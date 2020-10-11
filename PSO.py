from WingEvaluation import calc_fitness
from Util import rand

import copy

altitudes = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
speeds = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


# Range of m is [0, 9.5)
# Range of p is [0, 9)
# Range of t is [0, 40)

#array in order m, p, t
angle_of_attack = 3
mean_camber_length = 3
altitude_index = 8
speed_index = 8

particle_count = 3
iterations = 50

#Weights
omega = .5
phi_g = .5
phi_p = .5
learning_rate = .5


particle_current_positions = [None] * particle_count #x
particle_best_positions = [None] * particle_count  #p
particle_velocities = [None] * particle_count #v
particle_best_fitnesses = [None] * particle_count
swarm_best_position = [None] * 3 #g
swarm_best_fitness = 0

#calc_fitness(knots, altitude_feet, m, p, t, mean_camber_length)
for i in range(0, particle_count):
    print(i)
    particle_current_positions[i] = [rand(0, 9.5), rand(0, 9), rand(0, 40)]
    print(particle_current_positions[i])
    particle_best_positions = copy.deepcopy(particle_current_positions)

    print("start fitness calc")
    current_fitness = calc_fitness(speeds[speed_index], altitudes[altitude_index], particle_best_positions[i][0],particle_best_positions[i][1], particle_best_positions[i][2], mean_camber_length )
    print("end fitness calc")
    particle_best_fitnesses[i] = current_fitness

    if (current_fitness > swarm_best_fitness):
        swarm_best_fitness = current_fitness
        swarm_best_position = [particle_best_positions[i][0],particle_best_positions[i][1], particle_best_positions[i][2]]

    particle_velocities[i] = [rand(-9.5, 9.5), rand(-9, 9), rand(-40, 40)]

count = 0

while (count < iterations):
    count += 1
    print(count)
    for i in range(0, particle_count):
        for d in range(0, 3):
            r_p, r_g = rand(0, 1), rand(0, 1)

            particle_velocities[i][d] = omega * particle_velocities[i][d] + \
                                        phi_p * r_p * (particle_best_positions[i][d]-particle_current_positions[i][d]) + \
                                        phi_g * r_g * (swarm_best_position[d]-particle_current_positions[i][d])

        for d in range(0, 3):
            particle_current_positions[i][d] = particle_current_positions[i][d] + learning_rate * particle_velocities[i][d]

        print("start fitness calc")

        current_fitness = calc_fitness(speeds[speed_index], altitudes[altitude_index], particle_current_positions[i][0],particle_current_positions[i][1], particle_current_positions[i][2], mean_camber_length )

        print("end fitness calc")

        if (current_fitness > particle_best_fitnesses[i]):
            particle_best_fitnesses[i] = current_fitness
            if (particle_best_fitnesses[i] > swarm_best_fitness):
                swarm_best_position = particle_best_positions[i]

print(swarm_best_position)



#TODO Use numpy arrays instead of python arrays (Probably won't make a difference because calculating fitness is a massive bottleneck)