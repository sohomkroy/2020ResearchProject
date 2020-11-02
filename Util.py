import random

def get_reynolds_num(speed, length, kinematic_viscocity):
    return speed*length/kinematic_viscocity

def get_kinematic_velo(t_kelvin):
    #return 2.791*10**(-7)*t_kelvin**0.7355
    #print(t_kelvin)
    if (t_kelvin == 0):
        return 1.461e-5
    if (t_kelvin == 1000):
        return 1.581e-5
    if (t_kelvin == 2000):
        return 1.715e-5
    if (t_kelvin == 3000):
        return 1.863e-5
    if (t_kelvin == 4000):
        return 2.028e-5
    if (t_kelvin == 5000):
        return 2.211e-5
    if (t_kelvin == 6000):
        return 2.416e-5
    if (t_kelvin == 7000):
        return 2.646e-5
    if (t_kelvin == 8000):
        return 2.904e-5
    if (t_kelvin == 9000):
        return 3.196e-5
    if (t_kelvin == 10000):
        return 3.525e-5

    #if (t_kelvin == 0)

def c_to_k(c):
    return c
    #return c+273.15

def knots_to_ms(knots):
    return knots*.514444

def altitude_to_temp(altitude_feet):
    #return -0.002 * altitude_feet + 18.976
    return altitude_feet

def rand(a, b):
    return random.uniform(a, b)

