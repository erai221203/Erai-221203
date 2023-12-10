import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2pi with a step of 0.1
x = np.arange(0, 2*np.pi, 0.1)

# Calculate cos values for each x
y = np.sin(x)

# Plot the cos graph
plt.plot(x, y)

# Set the x and y axis labels
plt.xlabel('x')
plt.ylabel('cos(x)')

# Set the title of the graph
plt.title('Cos Graph')

# Show the graph
plt.show()
