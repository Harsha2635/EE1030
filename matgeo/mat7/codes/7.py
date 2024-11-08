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

    # Define y-values for plotting the parabola and the circle
    y_vals = np.linspace(-4 * a, 4 * a, 400)
    x_parabola = parabola(y_vals, a)
    x_circle_upper = circle(y_vals, a)
    x_circle_lower = -circle(y_vals, a)

    # Plot the curves for this value of 'a'
    plt.figure()
    plt.plot(x_parabola, y_vals, label=r'Parabola: $y^2 = 6 \cdot %.1f \cdot x$' % a, color='red')
    plt.plot(x_circle_upper, y_vals, label=r'Circle: $x^2 + y^2 = 16 \cdot %.1f^2$' % a, color='blue')
    plt.plot(x_circle_lower, y_vals, color='blue')

    # Fill the area between the curves for each value of 'a'
    y_shaded = np.linspace(y_int1, y_int2, 400)
    plt.fill_betweenx(y_shaded, parabola(y_shaded, a), circle(y_shaded, a), 
                      where=(circle(y_shaded, a) >= parabola(y_shaded, a)),
                      color='lightblue', alpha=0.5)

    # Labels and plot settings
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title(f'Area Enclosed by Parabola and Circle for a = {a}\nEnclosed Area = {area:.2f}')
    plt.grid(True)
    plt.legend()

    # Set equal aspect ratio and axis limits for a clearer view
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)

# Show the plots for both values of 'a'
plt.show()

