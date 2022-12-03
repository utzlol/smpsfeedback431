from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
a = 1

def p(x,y):
	a = float(x)*float(y)/(float(x)+float(y))
	return float(a)

v = input("volt : ")
rtot = input("rtot : ")
rout = input("rout : ")

while "p" in str(rtot):
	rtota = str(rtot).replace('p','iniganti',1).split("iniganti")[1]
	rtota = rtota.replace(")","iniganti",1).split("iniganti")[0]
	rtota = rtota.replace("(","").split(",")
	val = p(rtota[0], rtota[1])
	rtot = rtot.replace(f"p({str(rtota[0])},{str(rtota[1])})", str(val))
	rtot = eval(rtot)

print(rtot)

v = float(v)
rtot = float(rtot)
rout = float(rout)

itot = v/rtot
vout = v - rout*itot
print(vout)
