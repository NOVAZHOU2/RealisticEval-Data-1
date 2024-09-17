"""
Compute the dimensions of a rectangle enclosig a sphere.
Visualize the model_answer_result.

This code generated by ChatGPT. It is not exactly right,
but demonstrates some good things. Play around with it as
a starting point.

Would be great to be able to:
- model ellipsoids
- model spirals
- draw rectangles (clearly) around spheres, etc.
- demonstrate collision points.
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Sphere radius
r = 5.0

# Calculate the dimensions of the enclosing rectangle
length = width = height = 2 * r

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of points for the sphere's surface
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))

# Draw the sphere
ax.plot_surface(x, y, z, color='b', alpha=0.6)

# Set the axis limits based on the enclosing rectangle dimensions
ax.set_xlim([0, length])
ax.set_ylim([0, width])
ax.set_zlim([0, height])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()