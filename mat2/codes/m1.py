import matplotlib.pyplot as plt
import numpy as np

# Coordinates of the points
start_point = (0, 0)
west_point = (-5, 0)  # 5 meters due west
final_point = (-5, 12)  # 12 meters due north

# Compute the distance using Pythagorean theorem
distance = np.sqrt((final_point[0] - start_point[0])**2 + (final_point[1] - start_point[1])**2)

print(f"Distance from the starting point: {distance:.2f} meters")

# Plotting
plt.figure(figsize=(8, 6))
plt.plot([start_point[0], west_point[0]], [start_point[1], west_point[1]], 'bo-', label='West Movement')
plt.plot([west_point[0], final_point[0]], [west_point[1], final_point[1]], 'go-', label='North Movement')
plt.plot([start_point[0], final_point[0]], [start_point[1], final_point[1]], 'r--', label='Direct Distance')

plt.scatter(*start_point, color='black', zorder=5)
plt.scatter(*west_point, color='black', zorder=5)
plt.scatter(*final_point, color='black', zorder=5)

plt.text(start_point[0], start_point[1], 'Start', fontsize=12, ha='right')
plt.text(west_point[0], west_point[1], 'West', fontsize=12, ha='right')
plt.text(final_point[0], final_point[1], 'Final', fontsize=12, ha='right')

plt.xlabel('Meters')
plt.ylabel('Meters')
plt.title('Movement and Distance Calculation')
plt.axhline(0, color='grey', linewidth=0.5)
plt.axvline(0, color='grey', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

