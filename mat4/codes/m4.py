# Code by GVV Sharma
# Modified for Problem Solution - including point A
# Released under GNU GPL
# Constructing the Circle through B, C, D and Tangents from A

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Function to generate the circle points
def circ_gen(O, r):
    len = 100
    theta = np.linspace(0, 2*np.pi, len)
    x_circ = np.zeros((2, len))
    x_circ[0,:] = r * np.cos(theta)
    x_circ[1,:] = r * np.sin(theta)
    x_circ = x_circ + O
    return x_circ

# Function to generate line
def line_gen(P, Q):
    len = 100
    x_line = np.zeros((2,len))
    lambda_ = np.linspace(0,1,len)
    for i in range(len):
        temp1 = P + lambda_[i]*(Q-P)
        x_line[:,i] = temp1.T
    return x_line

# Coordinates for the triangle
A = np.array([6, 0]) # A(6, 0)
B = np.array([0, 0]) # B(0, 0)
C = np.array([0, 8]) # C(0, 8)

# Line AC (for calculation of D)
m_AC = (C[1] - A[1]) / (C[0] - A[0])
c_AC = A[1] - m_AC * A[0]

# Perpendicular from B to AC (finding point D)
# Slope of BD is perpendicular to AC
m_BD = -1 / m_AC

# Equation of BD: y = m_BD * x + c (c = 0, as it passes through B(0, 0))
# Set equation of BD equal to equation of AC to find D
# m_BD * x = m_AC * x + c_AC
x_D = c_AC / (m_BD - m_AC)
y_D = m_BD * x_D
D = np.array([x_D, y_D])

# Now generate the circle passing through B, C, and D
x1 = B.reshape(-1, 1)
x2 = C.reshape(-1, 1)
x3 = D.reshape(-1, 1)

# Line parameters
n = np.array([x2[1,0] - x1[1,0], x1[0,0] - x2[0,0]]).reshape(-1,1)  # Normal vector to BC
c = np.dot(n.T, x1)[0,0]  # Line constant

# Set up matrix to solve for the circle's center and radius
A_mat = np.block([[2*x1, 2*x2, n],[1, 1, 0]]).T
b = -np.array([LA.norm(x1)**2, LA.norm(x2)**2, c]).reshape(-1, 1)
x = LA.solve(A_mat, b)

# Centre and radius of the circle
u = x[:2]
O = -u  # Circle center
f = x[2][0]
r = np.sqrt(LA.norm(u)**2 - f)

print("Circle center: ", O)
print("Radius of the circle: ", r)

# Generating the circle points
x_circ = circ_gen(O, r)

# Generate lines AC and BD for visualization
x_AC = line_gen(A, C)
x_BD = line_gen(B, D)

# Plotting the triangle, circle, and tangents
plt.plot(x_AC[0,:], x_AC[1,:], label='Line AC')
plt.plot(x_BD[0,:], x_BD[1,:], label='Line BD')
plt.plot(x_circ[0,:], x_circ[1,:], label='Circle through B, C, D')

# Labeling coordinates
tri_coords = np.block([x1,x2,x3,O,A.reshape(-1,1)])  # Include A
plt.scatter(tri_coords[0,:], tri_coords[1,:], color='r')
vert_labels = ['$B$', '$C$', '$D$', '$O$', '$A$']  # Add A to labels
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
                 (tri_coords[0,i], tri_coords[1,i]), 
                 textcoords="offset points", 
                 xytext=(-10,5), ha='center')

# Tangent from A to the circle
# Equation of tangent from external point is not included in this code, but can be solved algebraically

# Final plot adjustments
plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid()
plt.legend()
plt.show()
