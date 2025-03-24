import pulp as p  # Asegúrate de importar el módulo


Lp_prob = p.LpProblem("Problem1", p.LpMaximize)

# Descision Variables
x1 = p.LpVariable("x1", lowBound=0)  # Crear variable x1 >= 0
x2 = p.LpVariable("x2", lowBound=0)  # Crear variable x2 >= 0
x3 = p.LpVariable("x3", lowBound=0)  # Crear variable x3 >= 0
X4 = p.LpVariable("x4", lowBound=0)  # Crear variable x3 >= 0

#objective function
Lp_prob += 3000 * x1 + 4000 * x2 + 4500 * x3 + 5000 * X4

#Constrainsts
Lp_prob += 2 * x1 + 1.5 * x2 + x3 <= 20
Lp_prob += 2 * x1 + x2 + 1.5 * x3 <= 24
Lp_prob += x1 + 2 * x2 + 0.5 * x3 <= 20

print(Lp_prob)

#Solving the linear programming problem
status = Lp_prob.solve()
print(p.LpStatus[status])

#Solucion
print(x1.value())
print(x2.value())
print(x3.value())
print(X4.value())











#print(f"x1 = {x1.value()}")
#print(f"x2 = {x2.value()}")
#print(f"x3 = {x3.value()}")
