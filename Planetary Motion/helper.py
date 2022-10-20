from vpython import *
from scipy import constants

class Helper:
    @staticmethod
    def heavenly_body(position, mass, radius, momentum, col):
        return sphere(pos=position, mass=mass, force=vector(0, 0, 0), radius=radius, color=col, momentum=momentum, make_trail=True, trail_radius=radius*0.1)


    @staticmethod
    def gravitational_force(body1, body2):
        r_vector = body1.pos - body2.pos
        force_magnitude = 1 * (body1.mass * body2.mass) / (mag(r_vector) ** 2)
        force_vector = -force_magnitude*hat(r_vector)
        return force_vector
