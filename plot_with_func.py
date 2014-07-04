

import math, pylab, scipy, numpy

g = 9.81
ax = 0
ay = -9.81
v0 = 30.0  # initial velocity
angle = 30.0 # launch angle (degrees)
#dt = 0.01  # time step 
dt= numpy.arange(0,5,0.001)   
pylab.xlim(0,80)
pylab.ylim(0,12)

old_dx = 0.0 # displacement dx (X-axis) at the initial position = 0
old_dy = 0.0 # displacement dy (Y-axis) at the initial position = 0
vx = v0*math.cos(angle*math.pi/180.0) # velocity vx (X-axis)
vy = v0*math.sin(angle*math.pi/180.0) # velocity vy (Y-axis)

i = 0 # counter

def calcul_displacement(dx,dy,vxi,vyi,dt):
    
    vxi,vyi = calcul_velocity(ax,ay,dt)
    dxi = dx + vxi*dt + (1/2)*ax*dt**2
    dyi = dy + vyi*dt + (1/2)*ay*dt**2
    return 2*dxi,2*dyi

def calcul_velocity(ax,ay,dt):
    vxi = vx + ax * dt 
    vyi = vy + ay * dt 
    return vxi,vyi



# MAIN

r=(2*vx*vy)/g # range of the shoot 
h=(v0*v0*(math.sin(math.radians(angle))**2))/(2*g) # height of the shoot

print"Range =", r, "meters"
print"Height =", h, "meters"

new_dx,new_dy=calcul_displacement(old_dx,old_dy,vx,vy,dt)
old_dx=new_dx
old_dy=new_dy
 
pylab.plot(new_dx,new_dy)
pylab.show()
