import random


class Problem:
    def __init__(self):
        # start with k random states
        self.initial_states = [random.randint(-10, 10) for _ in range(3)]

    # maximize this function
    def value(self, state):
        return -(state - 3) ** 2 + 10   # peak at state = 3

    def get_neighbors(self, state):
        return [state - 1, state + 1]


def local_beam_search(problem, k=3, max_iter=100):
    # Step 1: initialize k states
    states = problem.initial_states

    for _ in range(max_iter):
        all_neighbors = []

        # Step 2: expand all states
        for state in states:
            neighbors = problem.get_neighbors(state)
            all_neighbors.extend(neighbors)

        # Step 3: select k best states
        states = sorted(all_neighbors, key=lambda x: problem.value(x), reverse=True)[:k]

    # Step 4: return best state
    best = max(states, key=lambda x: problem.value(x))
    return best


# 🔥 MAIN
if __name__ == "__main__":
    problem = Problem()
    result = local_beam_search(problem)

    print("Final State:", result)
    print("Value:", problem.value(result))