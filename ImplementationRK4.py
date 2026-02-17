import numpy as np
from math import *

import matplotlib.pyplot as plt

def rk4(f, h, v, param):
    k_1=f(v, param)
    k_2=f(v+h/2*k_1, param)
    k_3=f(v+h/2*k_2, param)
    k_4=f(v+h*k_3, param)
    return v+h/6*(k_1+2*k_2+2*k_3+k_4)

def double_pendulum(v, param=[1,1,9.81]):
    phi1, phi2, p1, p2 = v
    m, l, g = np.array(param)
    cos_delta = cos(phi1-phi2)
    sin_delta = sin(phi1-phi2)
    c = (16-9*cos_delta*cos_delta)
    a = 6/(m*l*l*c)
    b = 3*a/c*(p1*p2*sin_delta*c-6*sin_delta*cos_delta*(p1**2+4*p2**2-3*p1*p2*cos_delta))
    return np.array([
        a*(2*p1-3*cos_delta*p2),
        a*(8*p2-3*cos_delta*p1),
        -b-3*m*g*l*sin(phi1)/2,
        b+m*g*l*sin(phi2)/2
    ])

def generate_trajectorie_rk4(f, h, n, v, param):
    traj = [v]
    for x in range(n):
        v = rk4(f, h, v, param)
        traj.append(v)
    return np.array(traj)

traj = generate_trajectorie_rk4(double_pendulum, 0.01, 10000, [pi/4,pi/4,1,1], [1,1,9.81])
print(traj)
plt.plot(traj[:,1],traj[:,2])
plt.show()
