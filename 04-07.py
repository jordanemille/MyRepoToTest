# file not functional yet

import math, pylab

ax = 0
ay = -9.81
v0 = 30.0  # initial velocity
angle = 30.0 # launch angle (degrees)
dt = 0.01  # time step 

dx0 = [0.0] # displacement dx (X-axis) at the initial position = 0
dy0 = [0.0] # displacement dy (Y-axis) at the initial position = 0
vx = [v0*math.cos(angle*math.pi/180.0)] # velocity vx (X-axis)
vy = [v0*math.sin(angle*math.pi/180.0)] # velocity vy (Y-axis)

i = 0 # counter

def calcul_displacement(vx,vy,dt):
    dx = dx0 + calcul_velocity(ax,ay,dt)[0]
    dy = dx0 + calcul_velocity(ax,ay,dt)[1]    
    return dx,dy

def calcul_velocity(ax,ay,dt):
    vx = v0 + ax * dt + (1/2) * ax * t**2
    vy = v0 + ay * dt + (1/2) * ay * t**2
    return vx,vy

# MAIN
while dy[i] >= 0.0:

    dx,dy=calcul_displacement(vx,vy,dt)
    pylab.plot(dx,dy)
    pylab.show()
    i = i+1
