from sympy.solvers import solve
from sympy import Symbol
import time

x = Symbol('x')
vc = 0
a = 1
done = 0
radd = 0
vtot = 0
def p(x,y):
	a = float(x)*float(y)/(float(x)+float(y))
	return float(a)

def getp(x):
	while "p" in str(x):
		xa = str(x).replace('p','iniganti',1).split("iniganti")[1]
		xa = xa.replace(")","iniganti",1).split("iniganti")[0]
		xa = xa.replace("(","").split(",")
		val = p(xa[0], xa[1])
		x = x.replace(f"p({str(xa[0])},{str(xa[1])})", str(val))
		x = eval(x)
	x = eval(str(x))
	return float(x)



#v = input("volt : ")
#rtot = input("rtot : ")
rtot = "p(20,510) + p(75,1.05) + 3.83"
rtot = getp(rtot)
#rout = input("rout : ")
rout = "p(20,510)"
rout = getp(rout)
rexcp = rtot - rout
#v = float(v)

#itot = v/rtot
#vout = v - rout*itot
#print(vout)

while done != 1:
#while "15.00" not in str(vtot):
#while True:
	routc = rout + radd
	#routc = p(rout,radd)
	rtotc = rexcp + routc
#	ic = v/rtotc
#	vc = v - ic*routc
	vtot = 2.5/(rexcp)*rtotc
	if radd > 20:
		done = 1
	radd = radd + 0.01
	#print(f"Vout : {vc}")
	print(vtot)
	print(f"Radd : {radd}")
	#print(rexcp)
	print(f"Rtotal : {rtotc}")
	print(f"Rout : {routc}")
	#time.sleep(0.1)
