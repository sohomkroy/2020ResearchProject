from WingGenerator import generate_wing
from LiftDragCalc import calc_lift_drag
from Util import get_reynolds_num, c_to_k, knots_to_ms, get_kinematic_velo, altitude_to_temp


def calc_fitness(knots, altitude_feet, m, p, t, mean_camber_length, angle_of_attack):
    file_name = "Wings/data.dat"
    scale_factor = mean_camber_length/generate_wing(m, p, t, 100, "./XFOIL6.99/" + file_name, False)
    #print(get_reynolds_num(knots_to_ms(knots), scale_factor, get_kinematic_velo(c_to_k(altitude_to_temp(altitude_feet)))))

    reynolds = int(get_reynolds_num(knots_to_ms(knots), scale_factor, get_kinematic_velo(c_to_k(altitude_to_temp(altitude_feet)))))
    #reynolds=3e6
    lift, drag = calc_lift_drag(file_name, reynolds, angle_of_attack)
    #print(lift)
    #print(drag)
    if (drag==0):
        drag = 10000000000
    return lift/drag
    #return (lift/drag)



#1760588	1163374	729707
#2112706	1396048	875649
#2464824	1628723	1021590
#2816941	1861398	1167532
#3169059	2094073	1313474
#3521177	2326748	1459415
#3873295	2559422	1605357
