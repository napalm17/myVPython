from vpython import *
from projectile import Projectile

def panel():
    scene.autoscale = True
    scene.center = vector(10, 10, 0)
    scene.height = 600
    scene.width = scene.height



if __name__ == '__main__':
    panel()
    my_projectile1 = Projectile(mass=1, radius=0.5, initial_height=33, initial_speed=10, initial_angle=(25, 60),
                                colour=color.red)
    my_projectile1.simulate()

    my_projectile2 = Projectile(mass=1, radius=0.5, initial_height=0, initial_speed=15, initial_angle=(80, 15),
                                colour=color.green)
    my_projectile2.simulate()


