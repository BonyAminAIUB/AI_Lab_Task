import random
import math


# Problem definition
class Problem:
    def __init__(self):
        self.initial_state = 0

    # here we MINIMIZE the function
    def value(self, state):
        return (state - 3) ** 2   # minimum at state = 3

    def get_neighbors(self, state):
        return [state - 1, state + 1]


# temperature decreasing function
def schedule(T):
    return T * 0.95   # gradually reduce temperature


def simulated_annealing(problem, T=10, Tmin=0.001):
    # Step 1: initial solution
    current = problem.initial_state

    # Step 2: repeat until temperature low
    while T > Tmin:

        # Step 3: pick random neighbor
        neighbors = problem.get_neighbors(current)
        next_state = random.choice(neighbors)

        # Step 4: compute Δ = f(new) - f(current)
        delta = problem.value(next_state) - problem.value(current)

        # Step 5: generate random number u
        u = random.random()

        # Step 6: decision rule (Pic-2 logic)
        if (delta < 0) or (math.exp(-delta / T) > u):
            current = next_state

        # Step 7: reduce temperature
        T = schedule(T)

    return current


if __name__ == "__main__":
    problem = Problem()
    result = simulated_annealing(problem)

    print("Final State:", result)
    print("Value:", problem.value(result))