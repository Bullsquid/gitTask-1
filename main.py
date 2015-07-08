import halves as h

def f(x):
    return (x+3) ** 2

a = -10
b = 10
eps = 0.0001
min = h.min_halves(f, a, b, eps)
print("x = %.3f; f(x) = %.3f" % (min["x"], min["f"]))