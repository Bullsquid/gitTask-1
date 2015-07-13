import numpy as np
import matplotlib.pyplot as plt


def min_halves(f, a, b, eps):

    if b < a:
        tmp = a
        a = b
        b = tmp

    t = np.arange(a-1.0, b+1.0, 0.02)
    right = []
    left = []
    plt.plot(t, f(t))
    while b-a >= eps:
        center = (a + b) / 2.0
        delta = (b-a) / 4.0
        x1 = center - delta
        x2 = center + delta
        if f(x1) < f(x2):

            b = x2
            right.append(x2)

        else:

            a = x1
            left.append(x1)

    plt.plot(right, map(f, right), 'rs')
    plt.plot(left, map(f, left), 'bs')
    plt.show()

    x_min = (a+b) / 2.0
    return {"x": x_min,
            "f": f(x_min)
            }