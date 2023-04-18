import math

# Initialize variables
approx_pi = 0
term = 0

# Create a table to store the approximations
table = [['Number of terms', 'Approximation of pi']]

# Approximate pi using the infinite series
for k in range(0, 10):
    term = ((-1)**k) / ((2*k) + 1)
    approx_pi += term
    approx_pi *= 4
    table.append([k+1, round(approx_pi, 6)])
    if approx_pi == 3.14:
        print(f"First 3.14 approximation after {k+1} terms")
    if approx_pi == 3.141:
        print(f"First 3.141 approximation after {k+1} terms")
    if approx_pi == 3.1415:
        print(f"First 3.1415 approximation after {k+1} terms")

# Print the table
for row in table:
    print(row)
