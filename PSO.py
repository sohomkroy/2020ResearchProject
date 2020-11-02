from WingEvaluation import calc_fitness
from WingGenerator import generate_wing
from Util import rand

import copy

altitudes = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
speeds = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


# Range of m is [0, 5)
# Range of p is [0, 9)
# Range of t is [0, 40)

#array in order m, p, t
angle_of_attack = 4.5
mean_camber_length = 3.048
altitude_index = 9
speed_index = 10

particle_count = int(input("particles"))
iterations = 100

#Weightsquit()
omega = float(input("omega"))
phi_g = float(input("phi_g"))
phi_p = float(input("phi_p"))
learning_rate = float(input("learning rate"))


particle_current_positions = [None] * particle_count #x
particle_best_positions = [None] * particle_count  #p
particle_velocities = [None] * particle_count #v
particle_best_fitnesses = [None] * particle_count
swarm_best_position = [None] * 3 #g
swarm_best_fitness = -1

#calc_fitness(knots, altitude_feet, m, p, t, mean_camber_length)
for i in range(0, particle_count):
    print(i)
    particle_current_positions[i] = [rand(0, 5), rand(0, 9), rand(5, 40)]
    #particle_current_positions[i] = [2, 4, 12]
    print(particle_current_positions[i])
    particle_best_positions[i] = particle_current_positions[i].copy()

    #print("start fitness calc")
    current_fitness = calc_fitness(speeds[speed_index], altitudes[altitude_index], particle_best_positions[i][0],particle_best_positions[i][1], particle_best_positions[i][2], mean_camber_length, angle_of_attack)
    print(current_fitness)
    #("end fitness calc")
    particle_best_fitnesses[i] = current_fitness

    if (current_fitness > swarm_best_fitness):
        swarm_best_fitness = current_fitness
        swarm_best_position = [particle_best_positions[i][0],particle_best_positions[i][1], particle_best_positions[i][2]]

    particle_velocities[i] = [rand(-5, 5), rand(-9, 9), rand(-40, 40)]
print(swarm_best_position)

count = 0

while (count < iterations):
    count += 1

    #print(str(count) + ": " + str(swarm_best_fitness) +"\t"+ str(swarm_best_position))
    print(str(swarm_best_fitness) + "\t" + str(swarm_best_position))
    #print(swarm_best_position)

    for i in range(0, particle_count):
        for d in range(0, 3):
            r_p, r_g = rand(0, 1), rand(0, 1)

            particle_velocities[i][d] = omega * particle_velocities[i][d] + \
                                        phi_p * r_p * (particle_best_positions[i][d]-particle_current_positions[i][d]) + \
                                        phi_g * r_g * (swarm_best_position[d]-particle_current_positions[i][d])

        #rand(0, 9.5), rand(0, 9), rand(0, 40)

        if (0 <= particle_current_positions[i][0] + learning_rate * particle_velocities[i][0] < 5):
            particle_current_positions[i][0] = particle_current_positions[i][0] + learning_rate * particle_velocities[i][0]
        elif (particle_current_positions[i][0] + learning_rate * particle_velocities[i][0] <= 0):
            particle_current_positions[i][0] = .0001
        else:
            particle_current_positions[i][0] = 5

        if (0 <= particle_current_positions[i][1] + learning_rate * particle_velocities[i][1] < 9):
            particle_current_positions[i][1] = particle_current_positions[i][1] + learning_rate * particle_velocities[i][1]
        elif (particle_current_positions[i][1] + learning_rate * particle_velocities[i][1] <= 0):
            particle_current_positions[i][1] = .0001
        else:
            particle_current_positions[i][1] = 9

        if (5 <= particle_current_positions[i][2] + learning_rate * particle_velocities[i][2] < 40):
            particle_current_positions[i][2] = particle_current_positions[i][2] + learning_rate * particle_velocities[i][2]
        elif (particle_current_positions[i][2] + learning_rate * particle_velocities[i][2] <= 5):
            particle_current_positions[i][2] = 5.0001
        else:
            particle_current_positions[i][2] = 40


        #print("start fitness calc")
        current_fitness = calc_fitness(speeds[speed_index], altitudes[altitude_index], particle_current_positions[i][0],particle_current_positions[i][1], particle_current_positions[i][2], mean_camber_length, angle_of_attack )
        #print(current_fitness, particle_current_positions[i])
        #print("end fitness calc")

        if (current_fitness > particle_best_fitnesses[i]):
            particle_best_fitnesses[i] = current_fitness
            if (particle_best_fitnesses[i] > swarm_best_fitness):
                if (particle_best_fitnesses[i] < 400):
                    swarm_best_position = particle_best_positions[i]
                    swarm_best_fitness = particle_best_fitnesses[i]

print(swarm_best_fitness)
print(swarm_best_position)

generate_wing(swarm_best_position[0],swarm_best_position[1], swarm_best_position[2], 100, "final_wing.txt", True)

import matplotlib.pyplot as plt

with open('final_wing.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]

import numpy as np

# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
#
# plt.scatter(x, y)
# plt.show()
#
# print(x)
# print(y)

with open('final_wing.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]

for i in range(0, len(x)):
    x[i] = float(x[i])

for i in range(0, len(y)):
    y[i] = float(y[i])


plt.xlim(-.2, 1.2)
plt.ylim(-1, 1)

plt.plot(x, y)
plt.show()
#print(calc_fitness(speeds[speed_index], altitudes[altitude_index], swarm_best_position[0],swarm_best_position[1], swarm_best_position[2], mean_camber_length, angle_of_attack ))


#TODO Use numpy arrays instead of python arrays (Probably won't make a difference because calculating fitness is a massive bottleneck)
#[4.7509586544629965, 5.211289742310498, 9.200534398522832]
#169.13284132841326

#[3.2965127187608876, 8.483742697903406, 7.910597965777982]
#169.5121951219512