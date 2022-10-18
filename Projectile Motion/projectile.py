from vpython import *
from helper import Helper
import plotter

class Projectile:
    dt = 1e-3
    t = 0
    ruler_counter = 0

    def __init__(self, mass, radius, colour, initial_height, initial_speed, initial_angle):
        self.mass = mass
        self.projectile = Helper.init_projectile(radius, initial_height, colour)
        self.velocity = Helper.init_velocity(initial_speed, initial_angle)
        self.gravitational_force = Helper.gravitational_force(mass)
        self.plot = plotter.Plot()

    def simulate(self):
        while self.projectile.pos.y >= 0:
            self.update_velocity()
            self.update_position()
            self.plot.update_plot(Projectile.t, (self.projectile.pos.x, self.projectile.pos.y, self.projectile.pos.z))
            self.add_ruler()

            rate(1000)
            Projectile.t += Projectile.dt  # update time

    def update_velocity(self):  # update velocity
        self.velocity += self.gravitational_force / self.mass * Projectile.dt

    def update_position(self):  # update position
        self.projectile.pos += self.velocity * Projectile.dt

    def add_ruler(self):        # add rulers
        if max(self.projectile.pos.x, self.projectile.pos.y, self.projectile.pos.z) >= Projectile.ruler_counter:
            box(pos=vector(Projectile.ruler_counter + 0.5, -0.05, 0), size=vector(0.95, 0.05, 0.05), color=color.white)
            box(pos=vector(-0.05, Projectile.ruler_counter + 0.5, 0), size=vector(0.05, 0.95, 0.05), color=color.white)
            box(pos=vector(-0.05, -0.05, Projectile.ruler_counter + 0.5), size=vector(0.05, 0.05, 0.95), color=color.white)
            Projectile.ruler_counter += 1

