import sympy
import numpy as np
import matplotlib.pyplot as plt
'''
# Define the symbolic variables and matrix
height = float(input("Enter the height: "))
length = float(input("Enter the length: "))
alpha = float(input("Enter the alpha value: "))
b = float(input("Enter the b value: "))
'''
height=1
length=1
alpha=1
b=1

rows, cols = 4, 5

num_nodes = 5
step_size = length / (num_nodes - 1)

symbolic_array = np.array([sympy.symbols(f'T{i}{j}') for i in range(rows) for j in range(cols)]).reshape(rows, cols)

matrix = sympy.Matrix(symbolic_array)
for i in range(rows):
    for j in range(cols):
        if i == 0 or j == 0:
            matrix[i, j] = 0
        elif i == 3:
            x = j * step_size
            matrix[i, j] = alpha * x

# Boundary Conditions
equations = []

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        equation = matrix[i + 1, j] - 4 * matrix[i, j] + matrix[i - 1, j] + matrix[i, j + 1] + matrix[i, j - 1]
        equations.append(equation)

# Additional equations
equation_1 = matrix[1, 4] - matrix[1, 3] - (b * length / 4)
equation_2 = matrix[2, 4] - matrix[2, 3] - (b * length / 4)
equations.extend([equation_1, equation_2])

variables=matrix.free_symbols
# Solve the system of equations
solution = sympy.solve(equations,variables)
# Create a function to map the variable symbols to their values
symbol_to_value = {symbol: value for symbol, value in solution.items()}


variables = matrix.free_symbols
# Convert the symbolic matrix to a matrix of values
result = sympy.solve(equations,variables)
#values = np.array([[symbol_to_value[matrix[i, j]] for j in range(cols)] for i in range(rows)], dtype=float)
print(result)
