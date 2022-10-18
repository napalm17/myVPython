from vpython import *
from pendulum import Pendulum
from random import randint


def window():
    scene.autoscale = True
    scene.center = vector(0, 0, 0)
    scene.height = 400
    scene.width = scene.height * 16 / 9


if __name__ == '__main__':
    window()
    my_pendulum = Pendulum(1, randint(-180, 180))
    my_pendulum.simulate()
