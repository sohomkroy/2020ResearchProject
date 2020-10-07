from WingEvaluation import calc_fitness
from Util import rand
import copy

altitudes = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
speeds = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


# Range of m is [0, 10)
# Range of p is [0, 10)
# Range of t is [0, 100)

#array in order m, p, t
angle_of_attack = 3
altitude_index = 8
speed_index = 8

particle_count = 100
iterations = 1000


particle_current_positions = [None] * particle_count
particle_best_positions = [None] * particle_count
particle_velocities = [None] * particle_count

for x in range(0, particle_count):
    particle_current_positions[x] = [rand(0, 10), rand(0, 10), rand(0, 100)]
    particle_best_positions = copy.deepcopy(particle_current_positions)

    if (calc_fitness(speeds[speed_index], altitudes[altitude_index], ))

print(particle_current_positions)
print(particle_best_positions)



