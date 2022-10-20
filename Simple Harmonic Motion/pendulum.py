from vpython import *
import scipy.constants as constants
from helper import Helper
from plotter import Plot


class Pendulum:
    t = 0
    dt = 1e-1

    def __init__(self, length, init_angle):
        self.angular_acceleration = 0
        self.length = length
        self.angular_velocity = 0
        self.angle = init_angle
        self.bob = Helper.init_bob(self.length, self.angle)
        self.rod = Helper.init_rod(self.bob.pos)
        self.plot = Plot()

    def simulate(self):
        while True:
            rate(100)
            self.update_angular_acceleration()
            self.update_angular_velocity()
            self.update_angle()
            self.update_bob_position()
            self.rod.axis = self.bob.pos
            self.plot.update_plot(Pendulum.t, (self.bob.pos.x, self.bob.pos.y))
            Pendulum.t += Pendulum.dt

    def update_angular_acceleration(self):
        self.angular_acceleration = (-constants.g / self.length) * sin(radians(self.angle))

    def update_angular_velocity(self):
        self.angular_velocity += self.angular_acceleration * Pendulum.dt

    def update_angle(self):
        self.angle += self.angular_velocity * Pendulum.dt

    def update_bob_position(self):
        self.bob.pos = vector(self.length * sin(radians(self.angle)), -self.length * cos(radians(self.angle)), 0)
