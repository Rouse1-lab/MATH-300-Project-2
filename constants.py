from evaluator import c_f

# 1. Golden Ratio (phi) = 1 + 1/(1 + 1/(1 + ...))
# Source: Standard continued fraction representation
def const_phi(M):
    c0 = 1
    k = lambda n: 1
    l = lambda n: 1
    return c_f(c0, k, l, M)

# 2. Square Root of 2 = 1 + 1/(2 + 1/(2 + ...))
def const_sqrt2(M):
    c0 = 1
    k = lambda n: 1
    l = lambda n: 2
    return c_f(c0, k, l, M)

# 3. Euler's Number (e) = 2 + 1/(1 + 1/(2 + 2/(3 + 3/(4 + ...))))
# Source: Euler's continued fraction
def const_e(M):
    c0 = 2
    k = lambda n: 1 if n == 1 else n - 1
    l = lambda n: 1 if n == 1 else n
    return c_f(c0, k, l, M)

# 4. Pi (derived via Brouncker's formula for 4/pi)
# pi = 4 / (1 + 1^2/(2 + 3^2/(2 + 5^2/(2 + ...))))
def const_pi(M):
    c0 = 1.0
    k = lambda n: (2.0 * n - 1.0)**2
    l = lambda n: 2.0
    return 4.0 / c_f(c0, k, l, M)

# 5. Natural Log of 2 (ln 2)
# ln 2 = 1 / (1 + 1^2/(2 + 2^2/(3 + 3^2/(4 + ...))))
def const_ln2(M):
    c0 = 0.0
    k = lambda n: 1.0 if n == 1 else (n - 1.0)**2
    l = lambda n: 1.0
    return c_f(c0, k, l, M)