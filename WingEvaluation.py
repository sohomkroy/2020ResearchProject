from WingGenerator import generate_wing
from LiftDragCalc import calc_lift_drag
from Util import get_reynolds_num, c_to_k, knots_to_ms, get_kinematic_velo
knots = 120
temperature = 30

m = 2
p = 4
t = 12
mean_camber_length = 5

file_name = "Wings/data.dat"
scale_factor = mean_camber_length/generate_wing(m, p, t, 100, "./XFOIL6.99/" + file_name)
lift, drag = calc_lift_drag(file_name, get_reynolds_num(knots_to_ms(120), scale_factor, get_kinematic_velo(c_to_k(30))), 3)
print(lift/drag)


