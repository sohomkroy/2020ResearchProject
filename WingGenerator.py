import numpy as np
import math

#Generates wing geometry with unit chord length, returns mean camber length
def generate_wing(m, p, t, resolution, filename):
    m = m/100
    p = p/10
    t = t/100

    range1 = np.linspace(1,0,resolution)

    top_wing = []
    bottom_wing = []

    #generate coordinates
    for x in range1:
        y_t = 5*t*(0.2969*math.sqrt(x)-.1260*x-0.3516*math.pow(x, 2) + 0.2843*math.pow(x, 3) - 0.1015*math.pow(x, 4))

        if (p!=0):
            if (0<=x<=p):
                y_c = m/math.pow(p, 2)*(2*p*x-math.pow(x, 2))
            else:
                y_c = m/math.pow(1-p, 2)*((1-2*p)+2*p*x-math.pow(x, 2))

            if (0<=x<=p):
                dy_c_dx = 2*m/math.pow(p, 2)*(p-x)
            else:
                dy_c_dx = m/math.pow(1-p, 2)*(p-x)


            theta = math.atan2(dy_c_dx, 1)

            xU = x-y_t * math.sin(theta)
            yU = y_c+y_t * math.cos(theta)

            xL = x + y_t * math.sin(theta)
            yL = y_c - y_t * math.cos(theta)
        else:
            xU=x
            xL=x
            yU=y_t
            yL=-y_t


        top_wing.append(str(xU) + '     ' + str(yU))
        bottom_wing.append(str(xL) + "     " + str(yL))

    bottom_wing = bottom_wing[::-1]
    del bottom_wing[0]

    #write to file
    f = open(filename, "w")
    f.write(filename + "\n")
    f.write("\n".join(top_wing))
    f.write("\n")
    f.write("\n".join(bottom_wing))

    f.close()

    if (p != 0):
        # from 0 to p
        front_mean_camber_length = (1/2*(p-p)*math.sqrt((4*m**2*(p-p)**2+p**4)/p**4)-p**2*math.asinh(2*m*(p-p)/p**2)/(4*m)) \
                                   - (1/2*(0-p)*math.sqrt((4*m**2*(p-0)**2+p**4)/p**4)-p**2*math.asinh(2*m*(p-0)/p**2)/(4*m))
        #from p to 1
        back_mean_camber_length = (1/2*(1-p)*math.sqrt(((4*m**2+6)*p**2-4*p*(2*m**2*1+1)+4*m**2*1**2+p**4-4*p**3+1)/(p-1)**4)-(p-1)**2*math.asinh(2*m*(p-1)/(p-1)**2)/(4*m)) \
                                  - (1/2*(p-p)*math.sqrt(((4*m**2+6)*p**2-4*p*(2*m**2*p+1)+4*m**2*p**2+p**4-4*p**3+1)/(p-1)**4)-(p-1)**2*math.asinh(2*m*(p-p)/(p-1)**2)/(4*m))

        mean_camber_length = front_mean_camber_length+back_mean_camber_length
    else:
        mean_camber_length = 1
    return mean_camber_length


generate_wing(2, 1, 24, 100, "./XFOIL6.99/" + "wing1")