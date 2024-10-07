# Code by GVV Sharma

# Modified for Problem Solution

# Released under GNU GPL

# Calculating area enclosed between curves

import sys  
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Read the values of 'a' from the C-generated text file using numpy.loadtxt
data = np.loadtxt('data.txt')
a_values = data  

# Define the equations for the curves
def parabola(x):
    return x**2 / 4  # From y^2 = 4x => y = sqrt(4x)

def reverse_parabola(x):
    return 2 * np.sqrt(x)  # From x^2 = 4y => y = x^2 / 4

# Find the intersection points
y_int1, y_int2 = 0, 4

# Compute the areas
area_between_curves, _ = quad(lambda y: reverse_parabola(y) - parabola(y), y_int1, y_int2)

# Area above the upper curve (parabola in this case)
area_above = quad(lambda y: 4 - parabola(y), y_int1, y_int2)[0]

# Area below the lower curve (reverse parabola)
area_below = quad(lambda y: reverse_parabola(y), y_int1, y_int2)[0]


# Visualization
y_vals = np.linspace(0, 4, 400)
x_parabola = parabola(y_vals)  # Curve from y^2 = 4x
x_reverse_parabola = reverse_parabola(y_vals)  # Curve from x^2 = 4y

plt.plot(x_parabola, y_vals, label='Curve: $y^2=4x$', color='r')
plt.plot(x_reverse_parabola, y_vals, label='Curve: $x^2=4y$', color='g')

# Fill the area between the curves
plt.fill_betweenx(y_vals, x_parabola, x_reverse_parabola,
                  where=(x_reverse_parabola >= x_parabola), color='gray', alpha=0.5, 
                  label=f'Area between curves: {area_between_curves:.4f}')

# Fill the area above the lower curve
plt.fill_betweenx(y_vals, 0, x_reverse_parabola,
                  where=(x_reverse_parabola >= 0), color='blue', alpha=0.2, 
                  label=f'Area below curve $y^2=4x$: {area_between_curves:.4f}')

# Fill the area below the upper curve
plt.fill_betweenx(y_vals, x_parabola, 4,
                  where=(x_parabola <= 4), color='orange', alpha=0.2, 
                  label=f'Area above curve $y^2=4x$: {area_between_curves:.4f}')

# Labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Area Enclosed by the Curves')
plt.grid(True)

# Position legend at the top left corner
plt.legend(loc='upper right')

# Set equal aspect ratio
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()

