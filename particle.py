# created on 16.10.2022

from vpython import *
from scipy.constants import *


class Particle:
    def __init__(self, position, velocity, mass, charge, spin):
        self.spin = spin
        self.charge = charge
        self.mass = mass
        self.velocity = velocity
        self.position = position
        self.body = sphere(pos=position, radius=0.1, color=color.yellow)

    def linear_momentum(self):  # p = m * v
        return self.mass * self.velocity

    def rest_energy(self):  # E = m * c ^ 2
        return self.mass * (speed_of_light ** 2)


electron = Particle(position=vector(0, 0, 0), velocity=vector(0, 0, 0), mass=electron_mass, spin=0.5,
                    charge=elementary_charge)
