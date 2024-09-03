# Run this script inside blender to generate cubes according
# to the list of cubes below. Used to visualise and solve part 1.
# Just output the blocks as a python tuple pair and past them in
# below.
#
# Content of this file was mostly generated by ChatGPT.

import bpy
from mathutils import Vector


def create_cube(coord1, coord2):
    # Create cube mesh.
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
    cube = bpy.context.active_object

    # Calculate the dimensions of the cube.
    dimensions = [abs(coord2[i] - coord1[i]) + 1 for i in range(3)]

    # Set the scale of the cube based on the dimensions.
    cube.scale = [dim / 2 for dim in dimensions]

    # Calculate the center of the cube.
    center = [(coord1[i] + coord2[i]) / 2 for i in range(3)]

    # Set the location of the cube.
    cube.location = Vector(center)


# Uncomment blow to also clear existing mesh objects in the scene.
# bpy.ops.object.select_all(action="DESELECT")
# bpy.ops.object.select_by_type(type="MESH")
# bpy.ops.object.delete()

cubes = [
    # Paste cubes here, cube should look something like `((1,0,3),(1,4,3))`.
]

# Create the cubes based on the given coordinates,
for point0, point1 in cubes:
    create_cube(point0, point1)