import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

# Define the equations of the parabola and the circle

# Parabola: y^2 = 4x, or equivalently x = y^2 / 4
def parabola(y):
    return y**2 / 4

# Circle: 4x^2 + 4y^2 = 9, or equivalently x^2 + y^2 = 9/4, so x = sqrt(9/4 - y^2)
def circle(y):
    return np.sqrt(9/4 - y**2)

# Find the points of intersection
def find_intersections():
    # Solve for y where the parabola and circle intersect
    def equations(y):
        return circle(y) - parabola(y)
    
    # Use fsolve to find the y-values where the curves intersect
    y1 = fsolve(equations, -1)[0]  # Initial guess around -1
    y2 = fsolve(equations, 1)[0]   # Initial guess around 1
    return y1, y2

y_int1, y_int2 = find_intersections()

# Compute the area between the curves using integration
def area_between_curves(y):
    return circle(y) - parabola(y)

# Perform the integration from y_int1 to y_int2
area, _ = quad(area_between_curves, y_int1, y_int2)

print(f"Area enclosed between the parabola and the circle: {area}")

# Visualization

# Generating points for the parabola and circle
y_vals = np.linspace(-np.sqrt(9/4), np.sqrt(9/4), 400)  # Extending y-range to cover the whole circle
x_parabola = parabola(y_vals)
x_circle_upper = circle(y_vals)

# Generating the lower half of the circle
x_circle_lower = -circle(y_vals)

# Plot the curves
plt.plot(x_parabola, y_vals, label=r'Parabola: $y^2 = 4x$', color='r')

# Plot the complete circle (upper and lower parts combined) with a single label
plt.plot(x_circle_upper, y_vals, label=r'Circle: $4x^2 + 4y^2 = 9$', color='b')
plt.plot(x_circle_lower, y_vals, color='b')

# Fill the area between the parabola and the upper half of the circle
plt.fill_betweenx(y_vals, x_parabola, x_circle_upper, where=(x_circle_upper >= x_parabola), color='lightblue', alpha=0.5)

# Adjusting the plot limits to show the complete graph
plt.xlim(-1.5, 3)
plt.ylim(-1.7, 1.7)

# Labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Area Enclosed by the Parabola and Circle')
plt.grid(True)
plt.legend()

# Equal aspect ratio to prevent distortion
plt.gca().set_aspect('equal', adjustable='box')

# Show plot
plt.show()

