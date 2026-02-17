import numpy as np
from math import *

def rk4(v, h, f, param):
    k_1=f(v, param)
    k_2=f(v+h/2*k_1, param)
    k_3=f(v+h/2*k_2, param)
    k_4=f(v+h*k_3, param)
    return v+h/6*(k_1+2*k_2+2*k_3+k_4)

def double_pendulum(v, param):
    ph11, phi2, p1, p2 = v
