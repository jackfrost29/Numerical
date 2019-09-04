# importing matplotlib module  
from matplotlib import pyplot as plt
import numpy


def f(x):
	return float(x)*x - 4*x - 10;


# x^2 - 4x - 10 = 0 = y = root

'''
plt.grid(True, which="both")
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
'''

plt.subplot(1, 2, 1)
x = numpy.linspace(2, 10, num=1000)
y = x * x - 4*x - 10
plt.plot(x, y)

n=10
x0 = 4
x1 = 9
# x2 = x1 - (f(x1) * ((x1-x0) / (f(x1) - f(x0))) )

print("--------USING FALSE POSITION METHOD-----------")
print("\n%-20s %-20s %-20s %-20s %-20s %-20s\n" % ("iter","x0","x1","x2","f(x2)","error"))

for i in range(1,n+1):
	x2 = x0 - (f(x0) * ( (x1-x0) / (f(x1)-f(x0))))
	f_x2 = f(x2)
	error = abs((x2-x1)/x2)

	var_1 = numpy.linspace(x0, x1, num=2)
	var_2 = numpy.linspace(f(x0), f(x1), num=2)
	plt.plot(var_1, var_2)

	var_1 = numpy.linspace(x2, x2, num=2)
	var_2 = numpy.linspace(0, f(x2), num=2)
	plt.plot(var_1, var_2)

	print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, x0, x1, x2, f_x2, error))

	if f_x2*f(x1) < 0:
		x0 = x2
	else:
		x1 = x2

plt.grid(True)

x0 = 4
x1 = 2

plt.subplot(1, 2, 2)
x = numpy.linspace(2, 10, num=1000)
y = x * x - 4*x - 10
plt.plot(x, y)

print("\n\n\n\n\n--------USING SECANT METHOD-----------")

print("\n%-20s %-20s %-20s %-20s %-20s %-20s\n" % ("iter","x0","x1","x2","f(x2)","error"))

for i in range(1,n+1):
	x2 = x1 - ( (f(x1) * (x1-x0)) / ( f(x1) - f(x0) ) )
	f_x2 = f(x2)
	error = abs((x2-x1)/x2)

	var_1 = numpy.linspace(x0, x1, num=2)
	var_2 = numpy.linspace(f(x0), f(x1), num=2)
	plt.plot(var_1, var_2)

	var_1 = numpy.linspace(x2, x2, num=2)
	var_2 = numpy.linspace(0, f(x2), num=2)
	plt.plot(var_1, var_2)

	print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, x0, x1, x2, f_x2, error))

	if f_x2*f(x1) < 0:
		x0 = x2
	else:
		x1 = x2

plt.grid(True)
plt.tight_layout()
plt.show()