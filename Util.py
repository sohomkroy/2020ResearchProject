import random

def get_reynolds_num(speed, length, kinematic_viscocity):
    return speed*length/kinematic_viscocity

def get_kinematic_velo(t_kelvin):
    return 2.791*10**(-7)*t_kelvin**0.7355

def c_to_k(c):
    return c+273.15

def knots_to_ms(knots):
    return knots*.514444

def altitude_to_temp(altitude_feet):
    return -0.002 * altitude_feet + 18.976

def rand(a, b):
    return random.uniform(a, b)

