import aiml

# Create the kernel and load the AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Define the initial state and the goal state
initial_state = 0
goal_state = 10

# Hill Climbing algorithm
current_state = initial_state
while current_state != goal_state:
    best_state = None
    best_heuristic = float('inf')

    # Generate neighboring states
    neighbors = [current_state - 1, current_state + 1]

    # Evaluate the heuristic for each neighbor
    for neighbor in neighbors:
        heuristic = abs(neighbor - goal_state)

        # Check if the heuristic is better than the current best
        if heuristic < best_heuristic:
            best_heuristic = heuristic
            best_state = neighbor

    # Update the current state
    current_state = best_state

    # Print the current state
    print("Current state:", current_state)

    # Get the AIML response for the current state
    response = kernel.respond(str(current_state))
    print("AIML response:", response)
