import math

a = -3
b = -2
eps = 0.01
max_itr = 100
x1 = (a + b) / 2  

x_prev = x1
for i in range(max_itr):
    if x_prev < 0:
        x_next = -abs(x_prev)**(1/3) - 1
    else:
        x_next = x_prev**(1/3) - 1

    error = abs(x_next - x_prev)
    
    print(f"Iteration {i+1}: x = {x_next:.5f}, error = {error:.5f}")
    
    if error < eps:
        print(f"\nConverged after {i+1} iterations with x = {x_next:.5f}")
        break

    x_prev = x_next

