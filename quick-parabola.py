import pylab
import scipy

g=9.81
v=65

x= scipy.linspace(0,8,100)
y=-1/2*g*x**2+v*x

pylab.plot(x,y)

pylab.ylim(0)

pylab.plot(5,0,marker='o', markersize=15)


pylab.show()
