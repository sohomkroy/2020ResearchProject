from WingGenerator import generate_wing
from WingEvaluation import calc_fitness
from LiftDragCalc import calc_lift_drag
import Util
#from PSO import mean_camber_length
#from PSO import angle_of_attack
#generate_wing(3.667534702567795, 3.3697783821577305, 7.836545651520241, 100, "owo.txt", True)

wing_params =  [[4.907627032155535, 2.285456846485068, 8.45272295949796],
[3.8746696502972826, 2.7775811865827182, 7.574126615087257],
[4.662867194338153, 4.298490221271511, 13.634831983875769],
[4.212054555232099, 3.28482922705467, 15.680815537725707],
[3.862909287810738, 2.7555030984533033, 6.721101758513292],
[3.993752243009368, 3.6849425254298316, 15.285159345980224],
[4.984804352500106, 2.3735673826237433, 10.439013464174643],
[4.773216888481903, 5.014635266570139, 15.180474353496596]
]

for x in range(5, 13):
    print(calc_fitness(x*10, 9000, wing_params[x-5][0], wing_params[x-5][1], wing_params[x-5][2], 3.048, 4.5))

# for x in range(5, 13):
#     #print(calc_fitness(x*10, 9000, 2, 4, 12, 3.048, 4.5))
#     knots = x*10
#     print(int(Util.get_reynolds_num(Util.knots_to_ms(knots), 3.048,
#                                     Util.get_kinematic_velo(Util.c_to_k(Util.altitude_to_temp(9000))))))

#for y in range (0, 12):
#    for x in range (5, 12):
#        knots = x * 10
#        scale_factor = 3.048
#        altitude_feet = y*1000
#        print(int(Util.get_reynolds_num(Util.knots_to_ms(knots), scale_factor, Util.get_kinematic_velo(Util.c_to_k(Util.altitude_to_temp(altitude_feet))))))
#    print()

#4.3507353346468935, 0.7944323333702826, 36.86270421820103

