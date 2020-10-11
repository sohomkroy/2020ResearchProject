from subprocess import Popen, PIPE
import os
import time

def calc_lift_drag(airfoil_path, reynolds, angle_of_attack):
    p = Popen("cmd.exe", stdin=PIPE, stdout=PIPE)
    p.stdin.write("cd XFOIL6.99\n".encode('ascii'))
    p.stdin.write(".\XFOIL\n".encode('ascii'))
    p.stdin.write(("LOAD ./"+airfoil_path+"\n").encode('ascii'))

    p.stdin.write("OPER\n".encode('ascii'))
    p.stdin.write("ITER 1000\n".encode('ascii'))
    p.stdin.write("VISC\n".encode('ascii'))
    p.stdin.write((str(reynolds)+"\n").encode('ascii'))
    #p.stdin.write("PACC\n".encode('ascii'))
    #p.stdin.write("\n".encode('ascii'))
    #p.stdin.write("\n".encode('ascii'))


    p.stdin.write(("A " + str(angle_of_attack) + "\n").encode('ascii'))
    #p.stdin.write("PWRT 1\n".encode('ascii'))
    #p.stdin.write((filename+"\n").encode('ascii'))
    p.stdin.write("\n".encode('ascii'))
    p.stdin.write("\n".encode('ascii'))
    time.sleep(1)
    sout, err = p.communicate(str('quit').encode('ascii'))
    #print(sout.decode("ascii").split())
    #print(sout.decode("ascii").split()[::-1])

    #print(sout.decode("ascii").split()[::-1][15])
    #print(sout.decode("ascii").split()[::-1][21])
    #os.remove(".\XFOIL6.99\\"+airfoil_path)
    #print(sout.decode("ascii").split()[::-1])

    #print(float(sout.decode("ascii").split()[::-1][21]), float(sout.decode("ascii").split()[::-1][15]))
    try:
        ret = float(sout.decode("ascii").split()[::-1][21]), float(sout.decode("ascii").split()[::-1][15])
    except:
        ret = 0, 1
    return ret



#print(calc_lift_drag("wing1", 3e6, 10))
