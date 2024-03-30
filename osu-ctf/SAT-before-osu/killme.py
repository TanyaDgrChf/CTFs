from sympy import symbols, Eq, solve

# Define the variables
b, c, w, t, d, u, p, e, v, l, j, a, m, h, o, q, x, n, g, f, s, i, k, r = symbols('b c w t d u p e v l j a m h o q x n g f s i k r')

# Define the equations
equations = [
    Eq(b + c + w, 314),
    Eq(t + d + u, 290),
    Eq(p + w + e, 251),
    Eq(v + l + j, 274),
    Eq(a + t + b, 344),
    Eq(b + j + m, 255),
    Eq(h + o + u, 253),
    Eq(q + l + o, 316),
    Eq(a + g + j, 252),
    Eq(q + x + q, 315),
    Eq(t + n + m, 302),
    Eq(d + b + g, 328),
    Eq(e + o + m, 246),
    Eq(v + v + u, 271),
    Eq(f + o + q, 318),
    Eq(s + o + j, 212),
    Eq(j + j + n, 197),
    Eq(s + u + l, 213),
    Eq(q + w + j, 228),
    Eq(i + d + r, 350),
    Eq(e + k + u, 177),
    Eq(w + n + a, 288),
    Eq(r + e + u, 212),
    Eq(q + l + f, 321)
]

# Solve the equations
solution = solve(equations)

# Display the solution
for var, val in solution.items():
    print(f"{var}: {val}")
