from vpython import *
import scipy.constants as constants


class Helper:   # contains methods that set the initial conditions of the system
    @staticmethod
    def init_velocity(speed, angle):
        return vector(speed * cos(radians(angle[0])) * cos(radians(angle[1])),
                      speed * sin(radians(angle[0])),
                      speed * sin(radians(angle[1])) * cos(radians(angle[0])))

    @staticmethod
    def init_projectile(radius, height, colour):
        return sphere(pos=vector(0, height, 0), radius=radius, color=colour, make_trail=True, trail_radius=0.1)

    @staticmethod
    def gravitational_force(mass):
        return vector(0, -mass * constants.g, 0)

