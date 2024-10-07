import numpy as np
import matplotlib.pyplot as plt

# Define the speeds
rain_speed = 35  # m/s (vertical)
bicycle_speed = 12  # m/s (horizontal)

# Velocity components
rain_velocity = np.array([0, -rain_speed])  # Rain moving downward
bicycle_velocity = np.array([-bicycle_speed, 0])  # Bicycle moving west

# Relative velocity of rain with respect to the woman
relative_velocity = rain_velocity + bicycle_velocity

# Calculate the angle to hold the umbrella
angle = np.arctan2(-relative_velocity[0], -relative_velocity[1])  # Angle in radians
angle_degrees = np.degrees(angle)  # Convert to degrees

# Print the result
print(f"The woman should hold her umbrella at an angle of {angle_degrees:.2f} degrees to the vertical.")

# Plotting the vectors
plt.quiver(0, 0, bicycle_velocity[0], bicycle_velocity[1], angles='xy', scale_units='xy', scale=1, color='b', label='Bicycle Velocity')
plt.quiver(0, 0, rain_velocity[0], rain_velocity[1], angles='xy', scale_units='xy', scale=1, color='g', label='Rain Velocity')
plt.quiver(0, 0, relative_velocity[0], relative_velocity[1], angles='xy', scale_units='xy', scale=1, color='r', label='Relative Rain Velocity')

# Set limits and labels
plt.xlim(-20, 5)
plt.ylim(-40, 5)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.title('Velocity Vectors of Bicycle and Rain')
plt.xlabel('West-East (negative is West, positive is East)')
plt.ylabel('Vertical (negative is Down)')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

