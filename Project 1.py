import math as math

def epsilon():
	eps = 1.0

	while (eps + 1 > 1):
		eps = eps / 2

	print("Epsilon Maquina:", eps)

def value_of_S():
	constant = 2

	for i in range (-15, -7):
		count = 0
		sum = 0

		while (1):
			aux = abs(((2**count)*(math.factorial(count)**2))/math.factorial(2*count+1))

			if (aux >= 10**i):
				sum += aux
				count = count + 1
			else: 
				break

		value_S = sum * constant
		error = abs(math.pi - value_S)

		print('Error:', 10**i, '| Absolut Error Actually Made:', error, '! Number of Terms:', count, '|S:', '%.16f' % value_S)

def eular_constant():
	sum = 0

	for i in range (1, 16):
		aux = abs((1+(1/(10**i)))**(10**i))
		value_E = aux
		print('Euler Constant ( m =', i, '):', '%.16f' % value_E)

	print('\n\n')

	for i in range (1, 21):
		j = 0
		sum = 0

		while j <= i:
			aux = abs(1/math.factorial(j))
			sum = sum + aux
			j = j + 1

		value_E = sum

		print('Euler Constant ( m =', i, '):', '%.16f' % value_E)

epsilon()
value_of_S()
eular_constant()