from vpython import *
from projectile import Projectile
from random import randint


def window():
    scene.autoscale = True
    scene.center = vector(10, 10, 0)
    scene.height = 900
    scene.width = scene.height * 16 / 9


if __name__ == '__main__':
    window()
    for col in [color.red, color.green, color.cyan]:
        my_projectile = Projectile(mass=1, radius=0.5, initial_height=0, initial_speed=randint(10, 50),
                                   initial_angle=(randint(0, 90), randint(0, 90)),
                                   colour=col)
        my_projectile.simulate()
