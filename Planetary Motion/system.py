from vpython import *
from scipy import constants
from helper import Helper


class System:
    t = 0
    dt = 1e-4

    def __init__(self, mass, pos, radius, momentum):
        self.star = Helper.heavenly_body(pos[0], mass[0], radius[0], momentum[0], color.yellow)
        self.planet = Helper.heavenly_body(pos[1], mass[1], radius[1], momentum[1], color.cyan)

    def simulate(self):
        while mag(self.star.pos - self.planet.pos) > 0.1:

            rate(1000)
            self.star.force = Helper.gravitational_force(self.star, self.planet)
            self.planet.force = Helper.gravitational_force(self.planet, self.star)

            self.star.momentum += self.star.force * System.dt
            self.planet.momentum += self.planet.force * System.dt

            self.star.pos += (self.star.momentum / self.star.mass) * System.dt
            self.planet.pos += (self.planet.momentum / self.planet.mass) * System.dt

            System.t += System.dt
