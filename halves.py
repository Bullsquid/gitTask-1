def min_halves(f, a, b, eps):

    if b < a:
        tmp = a
        a = b
        b = tmp

    length = b - a
    center = (a + b) / 2.0
    delta = length / 4.0
    x1 = center - delta
    x2 = center + delta

    if f(x1) < f(x2):

        if (x2 - a) < eps:

            x_min = (x2 + a) / 2.0

            return {"x": x_min,
                    "f": f(x_min)
                    }

        else:
            return min_halves(f, a, x2, eps)

    else:
        if (b - x1) < eps:

            x_min = (b + x1) / 2.0

            return {"x": x_min,
                    "f": f(x_min)
                    }

        else:

            return min_halves(f, x1, b, eps)


def f(x):
    return (x+3) ** 2

a = -10
b = 10
eps = 0.0001
min = min_halves(f, a, b, eps)
print(min)
