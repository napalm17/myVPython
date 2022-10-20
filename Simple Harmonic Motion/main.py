from vpython import *
from pendulum import Pendulum
from random import randint
from helper import Helper

if __name__ == '__main__':
    my_pendulum = Pendulum(1, randint(0, 180))
    my_pendulum.simulate()
