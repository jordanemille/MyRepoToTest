######################################################################
### This code comes from Internet and I brought some modifications ###
######################################################################

import math, pylab

#g = 9.81  # acceleration
ax = 0
ay = -9.81
v0 = 30.0  # initial velocity
angle = 30.0 # launch angle (degrees)
dt = 0.01  # time step 

dx = [0.0] # displacement dx (X-axis) at the initial position = 0
dy = [0.0] # displacement dy (Y-axis) at the initial position = 0
vx = [v0*math.cos(angle*math.pi/180.0)] # velocity vx (X-axis)
vy = [v0*math.sin(angle*math.pi/180.0)] # velocity vy (Y-axis)

# use Euler's method to integrate projectile equations of motion
i = 0 # counter
while dy[i] >= 0.0: # while the projectile don't touch the ground

    # extend the lists by appending another point
    dx += [0.0] # dx = dx + [0.0]
    dy += [0.0] 
    vx += [0.0]
    vy += [0.0]


    # apply finite difference approx to equations of motion
    vx[i+1] = vx[i] + ax*dt
    vy[i+1] = vy[i] + ay*dt
    dx[i+1] = dx[i]+vx[i]*dt
    dy[i+1] = dy[i]+vy[i]*dt
    
    i = i+1


# plot the trajectory
pylab.plot(dx, dy)

pylab.title('trajectory of a projectile')
pylab.xlabel('dx (m)')
pylab.ylabel('dy (m)')
pylab.ylim(ymin=0.0)
pylab.show()

