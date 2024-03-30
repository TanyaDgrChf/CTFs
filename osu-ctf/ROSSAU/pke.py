from sympy import mod_inverse

# Given values
e = 876603837240112836821145245971528442417
p = 99132954671935298039
q = 59644326261100157131

# Compute phi(n)
phi_n = (p - 1) * (q - 1)

# Calculate the private key exponent (d)
d = mod_inverse(e, phi_n)

print("Private key exponent (d) is:", d)
