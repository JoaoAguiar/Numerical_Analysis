import math

def formula(x):    
    return math.sin(math.pow(x, 2)) + 1.1 - math.pow(math.e, -x)

def formula_derivative(x):
    return 2*x*math.cos(math.pow(x, 2)) + math.pow(math.e, -x)

def bisection_method(formula, a, b, epsilon):
    m = a
    vfa = formula(a)
    error = abs(b - a)
    iterations = 0

    while (error > epsilon):
        print("x=" + str(m))

        iterations = iterations + 1
        m = (a+b) / 2

        if (formula(m) == 0):
            error = 0
        elif(formula(m)*vfa < 0):
            b = m
        else:
            a = m
        
        error = error / 2

    print("\nValue:" + str(m), "| Number of Iterations:" + str(iterations))
    print("Aproximation -> " + str(m), "± " + str(5*10**-9))
    
    return 

def simple_iteractive_method(formula, x_0, n_max, epsilon):
    iterations = 1

    while (iterations <= n_max):
        print("x=" + str(x_0))

        x_1 = formula(x_0)
        
        error = abs(x_1 - x_0)
        
        if (error < epsilon):
            print("\nValue:" + str(x_1), "| Number of Iterations:" + str(iterations))
            print("Aproximation -> " + str(x_1), "± " + str(5*10**-9))

            return
        
        iterations = iterations + 1
        x_0 = x_1
    
    print("\nNot possible to find any solution after " + str(n_max) + " iteractions")
    return

def newtons_method(formula, formula_derivative, x_0, n_max, epsilon):
    iterations = 1
    
    while (iterations < n_max):
        print("x=" + str(x_0))

        x_1 = formula(x_0)
        x_1_derivative = formula_derivative(x_0)

        if (abs(x_1_derivative) < epsilon):
            return

        x_1 = x_0 - (x_1/x_1_derivative)
        error = abs(x_1 - x_0)
        
        if (error < epsilon):
            print("\nValue:" + str(x_1), "| Number of Iterations:" + str(iterations))
            print("Aproximation -> " + str(x_1), "± " + str(5*10**-9))
        
            return

        iterations = iterations + 1
        x_0 = x_1

    print("\nNot possible to find any solution after " + str(n_max) + " iteractions")
    
    return

print("\n########## BISECTION ##########")
bisection_method(formula, -0.2, -0.1, 5*10**-9)
print("\n########## NEWTONS ##########")
newtons_method(formula, formula_derivative, -0.2, 25, 5*10**-9)
print("\n########## SIMPLE ITERACTIVE ##########")
simple_iteractive_method(formula, 0.5, 25, 5*10**-12)
