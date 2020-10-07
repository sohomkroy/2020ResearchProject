from WingGenerator import generate_wing
from LiftDragCalc import calc_lift_drag
from Util import get_reynolds_num, c_to_k, knots_to_ms, get_kinematic_velo, altitude_to_temp


def calc_fitness(knots, altitude_feet, m, p, t, mean_camber_length):
    file_name = "Wings/data.dat"
    scale_factor = mean_camber_length/generate_wing(m, p, t, 100, "./XFOIL6.99/" + file_name)
    lift, drag = calc_lift_drag(file_name, get_reynolds_num(knots_to_ms(knots), scale_factor, get_kinematic_velo(c_to_k(altitude_to_temp(altitude_feet)))), 3)
    return (lift/drag)



