from vpython import *
from system import System
from random import randint

if __name__ == '__main__':
    masses = (1000, 1)
    positions = (vector(0, 0, 0), vector(0, 1, 0))
    radius = (0.05, 0.02)
    momentums = (vector(0, 0, 0), vector(30, 0, 0))
    my_system = System(masses, positions, radius, momentums)
    my_system.simulate()
