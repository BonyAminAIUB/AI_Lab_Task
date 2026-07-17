import random

def get_neighbors(state):
    
    return [state - 1, state + 1]

def objective_function(x):

    return -x**2 + 10

def hill_climbing(initial_state):
    current = initial_state

    while True:
        neighbors = get_neighbors(current)
        next_state = max(neighbors, key=objective_function)

        if objective_function(next_state) <= objective_function(current):
            return current

        current = next_state



initial_state = random.randint(-10, 10)
result = hill_climbing(initial_state)
print("Hill Climbing Result:", result)


