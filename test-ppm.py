# test-ppm.py
# (c) 2024-06-28, Philip D Loewen

from PrettyPrinter import ppm
import numpy as np

A0 = 2.*np.random.rand(3,3) - np.ones((3,3))

print(" ")

A = A0/10
ppm(A,"A0 / 10")

print(" ")

ppm(A0,"A0")

print(" ")


A10 = A0*10
ppm(A10,"A10 = A0 * 10")

print(" ")

A100 = A0*100
ppm(A100,"A100 = A0 * 100")

print(" ")

A1000 = A0*1000
ppm(A1000,"A1000 = A0 * 1000")

print(" ")

A10000 = A0*10000
ppm(A10000,"A10000 = A0 * 10000")

print(" ")

Abig = A0*1E23
ppm(Abig,"Abig")


print(" ")

Atiny = A0*1E-11
ppm(Atiny,"Atiny")


print(" ")

B = np.array([1,2,3,4,5]) - 0.6
ppm(B,"B")

print(" ")

D = np.random.rand(3,3,3)
ppm(D,"D")

print(" ")

C = np.pi
ppm(C,"C")

A10000 = A0*10000
ppm(A10000,"A10000 = A0 * 10000",sigfigs=6)
ppm(A10000,"A10000 = A0 * 10000",sigfigs=5)
ppm(A10000,"A10000 = A0 * 10000",sigfigs=4)
ppm(A10000,"A10000 = A0 * 10000",sigfigs=3)
ppm(A10000,"A10000 = A0 * 10000",sigfigs=2)
ppm(A10000,"A10000 = A0 * 10000",sigfigs=1)
ppm(A10000,"A10000 = A0 * 10000",sigfigs=0)
ppm(A10000,"A10000 = A0 * 10000",sigfigs=48)

