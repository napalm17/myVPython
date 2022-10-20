from vpython import *
from helper import Helper
from plotter import Plot


class Projectile:
    t = 0
    dt = 1e-3
    ruler_counter = 0

    def __init__(self, mass, radius, colour, initial_height, initial_speed, initial_angle):
        self.projectile = Helper.init_projectile(radius, initial_height, initial_speed, initial_angle, mass, colour)
        self.plot = Plot()

    def simulate(self):
        while self.projectile.pos.y >= 0:
            self.update_velocity()
            self.update_position()
            self.plot.update_plot(Projectile.t, (self.projectile.pos.x, self.projectile.pos.y, self.projectile.pos.z))
            self.add_ruler()

            rate(1000)
            Projectile.t += Projectile.dt  # update time

    def update_velocity(self):  # update velocity
        self.projectile.velocity += Helper.gravitational_force(self.projectile.mass) / self.projectile.mass * Projectile.dt

    def update_position(self):  # update position
        self.projectile.pos += self.projectile.velocity * Projectile.dt

    def add_ruler(self):        # add rulers
        if max(self.projectile.pos.x, self.projectile.pos.y, self.projectile.pos.z) >= Projectile.ruler_counter:
            box(pos=vector(Projectile.ruler_counter + 0.5, -0.05, 0), size=vector(0.95, 0.05, 0.05), color=color.white)
            box(pos=vector(-0.05, Projectile.ruler_counter + 0.5, 0), size=vector(0.05, 0.95, 0.05), color=color.white)
            box(pos=vector(-0.05, -0.05, Projectile.ruler_counter + 0.5), size=vector(0.05, 0.05, 0.95), color=color.white)
            Projectile.ruler_counter += 1