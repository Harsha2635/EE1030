# Code by GVV Sharma
# Modified for Problem Solution
# Released under GNU GPL
# Calculating area enclosed between curves
import sys  # For path to external scripts
sys.path.insert(0, '/home/harsha/assignments/matgeo/codes/CoordGeo')  # Path to my scripts
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

# Read the values of 'a' from the C-generated text file using numpy.loadtxt
data = np.loadtxt('data.txt')
a_values = data  # a_values will contain [1.0, 2.0]

# Define the equation of the parabola: y^2 = 6ax, which implies x = y^2 / (6a)
def parabola(y, a):
    return y**2 / (6 * a)

# Define the equation of the circle: x^2 + y^2 = 16a^2, which implies x = sqrt(16a^2 - y^2)
def circle(y, a):
    return np.sqrt(16 * a**2 - y**2)

# Find the points of intersection between the parabola and the circle
def find_intersections(a):
    def intersection_eq(y):
        return circle(y, a) - parabola(y, a)
    
    # Solve for the y values of intersection
    y_int1 = fsolve(intersection_eq, -4 * a)[0]
    y_int2 = fsolve(intersection_eq, 4 * a)[0]

    return y_int1, y_int2

# Compute the area between the curves using numerical integration
def area_between_curves(y, a):
    return circle(y, a) - parabola(y, a)

# Loop over each value of 'a' and compute the enclosed area
for a in a_values:
    y_int1, y_int2 = find_intersections(a)
    area, _ = quad(area_between_curves, y_int1, y_int2, args=(a,))
    print(f"Area enclosed between the parabola and the circle for a = {a}: {area}")

# Visualization

# Define y-values for plotting
y_vals = np.linspace(-8, 8, 400)

# Plot for each value of 'a'
colors = ['r', 'g']  # Different colors for each curve
for i, a in enumerate(a_values):
    # Generate points for the parabola and circle
    x_parabola = parabola(y_vals, a)
    x_circle_upper = circle(y_vals, a)
    x_circle_lower = -circle(y_vals, a)

    # Plot the curves
    plt.plot(x_parabola, y_vals, label=r'Parabola: $y^2 = 6 \cdot %.1f \cdot x$' % a, color=colors[i])
    plt.plot(x_circle_upper, y_vals, label=r'Circle: $x^2 + y^2 = 16 \cdot %.1f^2$' % a, color=colors[i])
    plt.plot(x_circle_lower, y_vals, color=colors[i])

    # Fill the area between the curves for each value of 'a'
    plt.fill_betweenx(y_vals, x_parabola, x_circle_upper, where=(x_circle_upper >= x_parabola), color=colors[i], alpha=0.2)

# Labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Area Enclosed by the Parabola and Circle for Different Values of a')
plt.grid(True)
plt.legend()

# Set equal aspect ratio to avoid distortion
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()

