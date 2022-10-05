#   05.10.2022

from vpython import *

def main():
    sphere_location = vector(0, 0, 0)
    box_location = vector(2, 0, 0)
    my_color = vector(255, 112, 0)

    my_sphere = sphere(pos=sphere_location,color=my_color, radius=0.5)
    #   my_box = box(pos=box_location, color=color.cyan, size=vector(1, 2, 3))
    dx = 0.01

    for i in range(10000):
        rate(1000)  # number of loops per second
        my_sphere.pos.x += dx

main()