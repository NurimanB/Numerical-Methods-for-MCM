import math

# x = (x+1)^3
#f(x) = x^3+3x^2+2x+1

def f(x):
    return x**3+3*(x**2)+2*x+1

def bisection(a, b, eps):
    if f(a) * f(b) >= 0:
        print("Wrong. f(a) and f(b) must have opposite signs.")
        return None

    itr = 0
    while (b - a) / 2 > eps:
        itr += 1 #iteration
        mean = (a + b) / 2 #arithmertic mean
        print(f"Iteration {itr}: a = {a}, b = {b}, mean = {mean}, f(mean) = {round(f(mean), 4)}")
        
        if f(mean) == 0:  
            return mean
        elif f(a) * f(mean) < 0:  
            b = mean
        else:  
            a = mean

    return (a + b) / 2 

a = -3
b = -2
eps = 0.01

root = bisection(a, b, eps)

if root is not None:
    print(f"The root found by bisection method is approximately: {root}")
