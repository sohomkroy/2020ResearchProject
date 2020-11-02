from WingGenerator import generate_wing
import matplotlib.pyplot as plt

wing_params =  [[4.907627032155535, 2.285456846485068, 8.45272295949796],
[3.8746696502972826, 2.7775811865827182, 7.574126615087257],
[4.662867194338153, 4.298490221271511, 13.634831983875769],
[4.212054555232099, 3.28482922705467, 15.680815537725707],
[3.862909287810738, 2.7555030984533033, 6.721101758513292],
[3.993752243009368, 3.6849425254298316, 15.285159345980224],
[4.984804352500106, 2.3735673826237433, 10.439013464174643],
[4.773216888481903, 5.014635266570139, 15.180474353496596]
]

plt.gray()
for x in range(0, len(wing_params)):
    generate_wing(wing_params[x][0], wing_params[x][1], wing_params[x][2], 50, "graph_log.txt", True)

    with open('graph_log.txt') as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]
        y = [line.split()[1] for line in lines]

    import numpy as np
    for i in range(0, len(x)):
        x[i] = float(x[i])

    for i in range(0, len(y)):
        y[i] = float(y[i])

    plt.plot(x, y)
    plt.gray()


plt.xlim(-.2, 1.2)
plt.ylim(-.7, .7)
#
# plt.plot(x, y)
#
# with open('graph_log1.txt') as f:
#     lines = f.readlines()
#     x = [line.split()[0] for line in lines]
#     y = [line.split()[1] for line in lines]
#
# import numpy as np
# for i in range(0, len(x)):
#     x[i] = float(x[i])
#
# for i in range(0, len(y)):
#     y[i] = float(y[i])

plt.style.use('grayscale')
# plt.plot(x, y)
plt.gray()
plt.show()
