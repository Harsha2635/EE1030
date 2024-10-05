# Code by GVV Sharma
# Modified for Problem Solution
# Released under GNU GPL
# Calculating area enclosed between curves
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

import sys  # For path to external scripts
sys.path.insert(0, '/home/harsha/assignments/matgeo/codes/CoordGeo')  # Path to my scripts

# Read the values from the C-generated text file using numpy.loadtxt
data = np.loadtxt('data.txt')

# Extracting parabola and circle parameters
p = data[0]  # Parabola parameter (y^2 = 4px)
r = data[1]  # Circle radius
h = data[2]  # Circle center x-coordinate
k = data[3]  # Circle center y-coordinate

# Parabola equation: y^2 = 4px, so x = y^2 / (4p)
def parabola(y, p):
    return y**2 / (4 * p)

# Circle equation: (x - h)^2 + (y - k)^2 = r^2, so x = h + sqrt(r^2 - (y - k)^2)
def circle(y, r, h, k):
    return h + np.sqrt(r**2 - (y - k)**2)

# Find the points of intersection between the parabola and the circle
def find_intersections(p, r, h, k):
    def intersection_eq(y):
        return circle(y, r, h, k) - parabola(y, p)

    y_int1 = fsolve(intersection_eq, -r)[0]
    y_int2 = fsolve(intersection_eq, r)[0]

    return y_int1, y_int2

# Get the intersection points
y_int1, y_int2 = find_intersections(p, r, h, k)

# Compute the area between the curves using integration
def area_between_curves(y, p, r, h, k):
    return circle(y, r, h, k) - parabola(y, p)

# Perform the integration from y_int1 to y_int2
area, _ = quad(area_between_curves, y_int1, y_int2, args=(p, r, h, k))

print(f"Area enclosed between the parabola and the circle: {area}")

# Visualization

# Generating points for the parabola and circle
y_vals = np.linspace(-r, r, 400)
x_parabola = parabola(y_vals, p)
x_circle_upper = circle(y_vals, r, h, k)

# Generate the lower half of the circle
x_circle_lower = h - np.sqrt(r**2 - (y_vals - k)**2)

# Plot the curves
plt.plot(x_parabola, y_vals, label=r'Parabola: $y^2 = 4x$', color='r')
plt.plot(x_circle_upper, y_vals, label=r'Circle: $(x - %.2f)^2 + (y - %.2f)^2 = %.2f^2$' % (h, k, r), color='b')
plt.plot(x_circle_lower, y_vals, color='b')  # Lower part of the circle (no extra label)

# Fill the area between the curves
plt.fill_betweenx(y_vals, x_parabola, x_circle_upper, where=(x_circle_upper >= x_parabola), color='lightblue', alpha=0.5)

# Labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Area Enclosed by the Parabola and Circle')
plt.grid(True)
plt.legend()

# Set equal aspect ratio to avoid distortion
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()

