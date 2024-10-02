# Program to plot an ellipse and shade the area bounded by the ellipse and the line
# Code by GVV Sharma
# August 8, 2020
# Revised July 31, 2024
# Revised August 16, 2024

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Read the values from the C-generated text file using numpy.loadtxt
data = np.loadtxt('data.txt')

# Extracting ellipse and line parameters
a = data[0]
b = data[1]
h = data[2]
k = data[3]
V = np.array([[data[4], data[5]], [data[6], data[7]]])  # Ellipse matrix
slope = data[8]
intercept = data[9]

# Function to generate points on the ellipse
def ellipse_gen(a, b, h, k):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = h + a * np.cos(theta)
    y = k + b * np.sin(theta)
    return x, y

# Function representing the ellipse equation
def ellipse_eq(x, y, a, b, h, k):
    return ((x - h) ** 2) / a**2 + ((y - k) ** 2) / b**2 - 1

# Function representing the line equation
def line_eq(x, slope, intercept):
    return slope * x + intercept

# Solving for intersection points between the ellipse and the line
def find_intersections(a, b, h, k, slope, intercept):
    # Define a function that returns the difference between the line and ellipse
    def equations(x):
        y = line_eq(x, slope, intercept)
        return ellipse_eq(x, y, a, b, h, k)
    
    # Use fsolve to find roots (i.e., intersection points)
    x1 = fsolve(equations, -a)  # Initial guess near -a
    x2 = fsolve(equations, a)   # Initial guess near a
    y1 = line_eq(x1, slope, intercept)
    y2 = line_eq(x2, slope, intercept)
    
    return (x1[0], y1[0]), (x2[0], y2[0])

# Get intersection points
(x_int1, y_int1), (x_int2, y_int2) = find_intersections(a, b, h, k, slope, intercept)

# Generating the ellipse
x_ellipse, y_ellipse = ellipse_gen(a, b, h, k)

# Line: y = slope * x + intercept
x_line = np.linspace(-a, a, 100)
y_line = slope * x_line + intercept

# Create arrays for shading between the intersection points
x_shaded = np.linspace(x_int1, x_int2, 100)
y_ellipse_shaded = np.sqrt(b**2 * (1 - (x_shaded - h)**2 / a**2)) + k  # Upper half of the ellipse
y_line_shaded = slope * x_shaded + intercept

# Plotting the ellipse and the line
plt.plot(x_ellipse, y_ellipse, label='Ellipse')
plt.plot(x_line, y_line, label='Line')

# Fill the area between the ellipse and the line
plt.fill_between(x_shaded, y_line_shaded, y_ellipse_shaded, where=(y_ellipse_shaded >= y_line_shaded),
                 interpolate=True, color='lightblue', alpha=0.5)

# Labels
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Shaded Area Between Ellipse and Line')
plt.grid()
plt.legend()

# Plot settings
plt.gca().set_aspect('equal', adjustable='box')

# Display the plot
plt.show()

