from evaluator import c_f

# 1. Exponential function: e^x via Lambert's continued fraction
# e^x = 1 + 2x / (2 - x + x^2 / (6 + x^2 / (10 + x^2 / (14 + ...))))
def func_exp(x, M):
    c0 = 1.0
    k = lambda n: 2 * x if n == 1 else x**2
    l = lambda n: 2.0 - x if n == 1 else 4.0 * n - 2.0
    return c_f(c0, k, l, M)

# 2. Tangent function: tan(x)
# tan(x) = x / (1 - x^2 / (3 - x^2 / (5 - x^2 / (7 - ...))))
def func_tan(x, M):
    c0 = 0.0
    k = lambda n: x if n == 1 else -x**2
    l = lambda n: 1.0 if n == 1 else 2.0 * n - 1.0
    return c_f(c0, k, l, M)

# 3. Hyperbolic Tangent: tanh(x)
# tanh(x) = x / (1 + x^2 / (3 + x^2 / (5 + x^2 / (7 + ...))))
def func_tanh(x, M):
    c0 = 0.0
    k = lambda n: x if n == 1 else x**2
    l = lambda n: 1.0 if n == 1 else 2.0 * n - 1.0
    return c_f(c0, k, l, M)

# 4. Arctangent: arctan(x)
# arctan(x) = x / (1 + 1^2*x^2 / (3 + 2^2*x^2 / (5 + 3^2*x^2 / (7 + ...))))
def func_arctan(x, M):
    c0 = 0.0
    k = lambda n: x if n == 1 else ((n - 1) * x)**2
    l = lambda n: 1.0 if n == 1 else 2.0 * n - 1.0
    return c_f(c0, k, l, M)

# 5. Square root function: sqrt(1 + x)
# sqrt(1 + x) = 1 + x / (2 + x / (2 + x / (2 + ...))) -> generalized form
def func_sqrt1p(x, M):
    c0 = 1.0
    k = lambda n: x
    l = lambda n: 2.0
    return c_f(c0, k, l, M)