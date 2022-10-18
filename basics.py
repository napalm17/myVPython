#  created on 05.10.2022

from vpython import *
import numpy as np


def main():
    animate(1000, 0.1, 100)


def animate(my_range, my_interval, frame_rate):
    my_gd = graph(xtitle="time", ytitle="x pos")    # create graph
    my_plot = gcurve(color=color.red)     # create plot


    my_vector = vector(1, 0, 0)
    print(mag(my_vector))                                   # magnitude of a vector
    print(my_vector.hat)                                    # unit vector

    my_sphere = sphere(pos=my_vector, color=vector(255, 112, 0),
                       radius=0.25, make_trail=True, trail_color=color.cyan,
                       opacity=0.5)                 # create an object

    my_curve = curve(pos=[vector(0, 0, 0), vector(1, 0, 0), vector(1, 1, 0)])
    my_curve.origin = my_vector

    my_label = label(pos=my_vector)
    dx = 0.1
    for t in np.arange(0, my_range, my_interval):
        rate(frame_rate)                            # number of loops per second

        if not(-np.pi < my_sphere.pos.x < np.pi):
            dx = -dx
        my_sphere.pos.x += dx
        my_sphere.pos.y = np.cos(my_sphere.pos.x)
        my_label.text = "pos x:{:.2f}".format(my_sphere.pos.x)
        my_plot.plot(pos=(t, my_sphere.pos.x))     # update graph


main()

