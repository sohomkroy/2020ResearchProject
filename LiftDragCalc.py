from subprocess import Popen, PIPE, STDOUT, check_output
import os
import time



def calc_lift_drag(airfoil_path, reynolds, angle_of_attack):
    p = Popen("cmd.exe", stdin=PIPE, stdout=PIPE)

    #print("started cmd")
    p.stdin.write("cd XFOIL6.99\n".encode('ascii'))
    p.stdin.write(".\XFOIL\n".encode('ascii'))
    p.stdin.write(("LOAD ./"+airfoil_path+"\n").encode('ascii'))
    #p.stdin.write(("NACA 2412").encode('ascii'))
    p.stdin.write(("\n").encode('ascii'))
    p.stdin.write(("PANE\n").encode('ascii'))


    p.stdin.write("OPER\n".encode('ascii'))
    p.stdin.write("ITER 300\n".encode('ascii'))
    p.stdin.write("VISC\n".encode('ascii'))
    p.stdin.write((str(reynolds)+"\n").encode('ascii'))

    #p.stdin.write("PACC\n".encode('ascii'))
    #p.stdin.write("\n".encode('ascii'))
    #p.stdin.write("\n".encode('ascii'))
    p.stdin.write(("A 0\n").encode('ascii'))

    p.stdin.write(("A .25\n").encode('ascii'))

    p.stdin.write(("A 0.5\n").encode('ascii'))

    p.stdin.write(("A .75\n").encode('ascii'))

    p.stdin.write(("A 1\n").encode('ascii'))

    p.stdin.write(("A 1.25\n").encode('ascii'))

    p.stdin.write(("A 1.5\n").encode('ascii'))

    p.stdin.write(("A 1.75\n").encode('ascii'))

    p.stdin.write(("A 2\n").encode('ascii'))

    p.stdin.write(("A 2.25\n").encode('ascii'))

    p.stdin.write(("A 2.5\n").encode('ascii'))

    p.stdin.write(("A 2.75\n").encode('ascii'))

    p.stdin.write(("A 3\n").encode('ascii'))

    p.stdin.write(("A 3.25\n").encode('ascii'))

    p.stdin.write(("A 3.5\n").encode('ascii'))

    p.stdin.write(("A 3.75\n").encode('ascii'))

    p.stdin.write(("A 4\n").encode('ascii'))

    p.stdin.write(("A 4.25\n").encode('ascii'))

    p.stdin.write(("A 4.5\n").encode('ascii'))
    #print("started test")

    #p.stdin.write("PWRT 1\n".encode('ascii'))
    #p.stdin.write((filename+"\n").encode('ascii'))
    p.stdin.write("\n".encode('ascii'))
    p.stdin.write("\n".encode('ascii'))
    p.stdin.write("\n".encode('ascii'))
    p.stdin.write("\n".encode('ascii'))

    #print("trying to quit")
    #output = check_output(cmd, stderr=STDOUT, timeout=seconds)
    try:
        sout, err = p.communicate(str('quit').encode('ascii'), timeout=10)
    except:
        p.kill()
        p.terminate()
        return 0, 1000

    #print("ended test")
    #print(sout.decode("ascii").split())
    arr = sout.decode("ascii").split()[::-1]

    if ("continue" in arr):
        if (arr[arr.index("continue")-1] == "failed"):
            return 0, 1000

    #print(arr)
    try:
        drag = arr[arr.index("CD")-2]
        lift = arr[arr.index("CL")-2]
    except:
        return 0, 1000

    #print()

    #print(sout.decode("ascii").split()[::-1][15])
    #print(sout.decode("ascii").split()[::-1][21])
    #os.remove(".\XFOIL6.99\\"+airfoil_path)
    #print(sout.decode("ascii").split()[::-1])


    try:
        ret = float(lift), float(drag)
    except:
        print("broke2")

        ret = 0, 1000

    return ret



#print(calc_lift_drag("wing1", 3e6, 10))
