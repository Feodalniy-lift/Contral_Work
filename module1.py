#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ученик
#
# Created:     25.01.2024
# Copyright:   (c) Ученик 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from math import pow


def decorator(frog):
    def wrapper(Vo,V,t):
        a=frog(Vo,V,t)
        print(a)
        S=Vo*t+(a*pow(t,2)/2)
        print(S)
    return wrapper

@decorator
def frog (Vo,V,t):
    a = (V-Vo)/t
    return a



try:
    frog(V=float(input()),Vo=float(input()),t=int(input()))



except (ZeroDivisionError,ValueError):
    print("вводите числа и время не может быть равно нулю")
    V=1
    Vo=10
    t=10
    a=(V-Vo)/t







