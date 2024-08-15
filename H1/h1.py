import numpy as np
import matplotlib.pyplot as plt

# Define the vectors
vector_a = np.array([0, -35])
vector_b = np.array([-12, 0])

# Add the vectors
vector_sum = vector_a - vector_b

# Print vectors and their sum in matrix format
print("Vector A:", vector_a)
print("Vector B:", vector_b)
print("Vector Sum:", vector_sum)

# Plot the vectors
plt.figure(figsize=(8, 8))

# Plot Vector A
plt.quiver(0, 0, vector_a[0], vector_a[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector A')

# Plot Vector B
plt.quiver(0, 0, vector_b[0], vector_b[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector B')

# Plot Vector Sum
plt.quiver(0, 0, vector_sum[0], vector_sum[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector Sum')

# Set plot limits
plt.xlim(-1, 7)
plt.ylim(-4, 5)

# Adding grid
plt.grid(True)

# Adding legend
plt.legend()

# Adding labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Adding title
plt.title('Vector Addition')

# Show plot
plt.show()
