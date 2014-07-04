from __future__ import division                                
from sympy import symbols, S, pi, solve, sin, cos
from sympy.plotting import plot_parametric
import math

g=9.81 # acceleration of gravity
v=int(raw_input("Choose the velocity of your shoot: ")) # velocity
o=int(raw_input("Choose the angle of your shoot: ")) # angle
t=symbols("t")

sin_degrees= math.sin(math.radians(o)) # sin(o) in degrees
cos_degrees=  math.cos(math.radians(o)) # cos(o) in degrees
tan_degrees= math.tan(math.radians(o)) # tan(o) in degrees

vz=v*sin_degrees # vz component (vertical) of the initial velocity
vx=v*cos_degrees # vx component (horizontal) of the initial velocity

r=(2*vx*vz)/g # range of the shoot 
h=(v*v*(sin_degrees*sin_degrees))/(2*g) # height of the shoot

print"Range =", r, "meters"
print"Height =", h, "meters"

z=(-1/2)*g*t**2 + vz*t # equation of z in function of the time
x=vx*t # equation of x in fucntion of the time

impact=solve(z,t) # solve z(t)=0
tMax=max(impact) # find the maximun solution

serie=(x,z,(t,0,tMax))
p=plot_parametric(serie)



