from __future__ import division
from sympy import symbols, S, pi, solve, sin, cos
from sympy.plotting import plot_parametric
import math

def shoot():

	g = 9.81
	series =  []
	cpt = 1

	for i in range(1): #5
		print	
		print"*****************"	
		print"Shoot number", cpt
		v=int(raw_input("Choose the velocity of your shoot: ")) # velocity
		alpha_deg=int(raw_input("Choose the angle of your shoot: ")) # angle
		print
		r=(2*v*math.cos(math.radians(alpha_deg))*v*math.sin(math.radians(alpha_deg)))/g # range of the shoot 
		h=(v*v*(math.sin(math.radians(alpha_deg))*math.sin(math.radians(alpha_deg))))/(2*g) # height of the shoot
		print"Range =", math.ceil(r), "meters"
		print"Height =", math.ceil(h), "meters"
		cpt+=1
		print

		t = symbols("t")
		alpha_rad = S(alpha_deg) * pi / 180
		z = v * sin(alpha_rad)*t - 1/2*g*t**2
 
		impact = solve(z,t)
		tMax = max(impact)
		x = v*cos(alpha_rad)* t
		serie = (x,z, (t,0,tMax))
		series.append(serie)

	p = plot_parametric(*series,  show=False)

	p[0].line_color = "red"
	#p[1].line_color = "purple"
	#p[2].line_color = "black"
	#p[3].line_color = "green"
	#p[4].line_color = "yellow"
	p.show()

	r=math.ceil(r)
	h=math.ceil(h)



	return r


def function(r):
	target=int(raw_input("X-axis of the target:"))
	if r==target:
		print"You destroyed the target!"
	else:
		print"You missed the target!"


# main
b=shoot()
function(b)


