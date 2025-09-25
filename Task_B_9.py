import math

x = 3.3
a = x*math.sin(2*x)
b = math.cos(2*x)
y = 3*x**2 * ((  (a/b) + (math.e**(-3*x)) * (x**2+4))**0.5)
print('x =',x)
print('y =',round(y,5))