from vpython import *
import scipy.constants as constants


class Helper:   # contains methods that set the initial conditions of the system
    @staticmethod
    def init_bob(length, angle):
        return sphere(pos=vector(length * sin(angle), -length * cos(angle), 0),
                      radius=0.1, color=color.orange, trail_radius=0.01, trail_color=color.red)

    @staticmethod
    def init_rod(bob_position):
        return cylinder(pos=vector(0, 0, 0), axi=bob_position, radius=0.01)

