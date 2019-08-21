# importing matplotlib module  
from matplotlib import pyplot as plt
import numpy
  

'''
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 
  
# Function to plot 
plt.plot(x,y) 
  
# function to show the plot 
plt.show()
'''

def f(x):
	return float(x)*x - 4*x - 10;


# x^2 - 4x - 10 = 0 = y = root



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
	print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, x0, x1, x2, f_x2, error))

	if f_x2*f(x1) < 0:
		x0 = x2
	else:
		x1 = x2

x0 = 4
x1 = 2

print("\n\n\n\n\n--------USING SECANT METHOD-----------")

print("\n%-20s %-20s %-20s %-20s %-20s %-20s\n" % ("iter","x0","x1","x2","f(x2)","error"))

for i in range(1,n+1):
	x2 = x1 - ( (f(x1) * (x1-x0)) / ( f(x1) - f(x0) ) )
	f_x2 = f(x2)
	error = abs((x2-x1)/x2)
	print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, x0, x1, x2, f_x2, error))

	if f_x2*f(x1) < 0:
		x0 = x2
	else:
		x1 = x2


x = numpy.array(range(-10,50))
y = x * x - 4*x - 10

plt.plot(x, y)
plt.grid(True, which="both")
plt.show()