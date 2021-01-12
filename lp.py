from scipy.optimize import linprog

# neg F values 
c = [-4, -3]
A = [[1, 3],
    [-1, 2]]
b = [9, 2]

res = linprog(c, A_ub = A, b_ub = b, bounds = (0, None))

# printing
print("Resultate gesamt:\n", res)
print("optimaler Wert:", -res.fun)
print("optimaler Punkt:", res.x)