import numpy as np
 
def f(x):
    return 5 * x**2 + np.sqrt(x)

def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    midpoints = np.linspace(a + h/2, b - h/2, n)
    return h * sum(f(midpoints))

def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's rule")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    return (h / 3) * (fx[0] + 4 * sum(fx[1:n:2]) + 2 * sum(fx[2:n-1:2]) + fx[-1])

a, b = 0, 3
n = 6

midpoint_result = midpoint_rule(f, a, b, n)
simpsons_result = simpsons_rule(f, a, b, n)

print(midpoint_result)
print(simpsons_result)
