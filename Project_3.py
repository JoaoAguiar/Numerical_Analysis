import math as math
import numpy as numpy

def yFunction(t): 
	return t/(1+math.pow(t, 2))

def yFunctionLine(y, t): 
	return ((t/(1+math.pow(t, 2))) - 2*math.pow(y, 2))

def euler(h, n, y, t):
	value = 0
	index = 0

	while(index <= n):
		value = y + h*yFunctionLine(y, t)
		y = value
		t = t + h
		index = index + 1
		
	exact_solution = yFunction(1)
	error = exact_solution - value

	print("")
	print("h =", h)
	print("n = ", n)
	print("Value = %.5f" %value)
	print("Exact Solution = %.5f" %exact_solution)
	print("Error = %.5f" %error)
	print("")

a = 0
b = 1
i = 0
h_values = numpy.array([0.2, 0.1, 0.05])

while i < 3:
	n = (b-a)/h_values[i]
	euler(h_values[i], n, 0, 0)
	i = i + 1