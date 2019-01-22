from sympy import *


def generate_k(n: int):
    k = Symbol('k')
    _k = N(solve((2 ** (n - k)) - 1 - n, k)[0])

    if _k % int(_k) != 0:
        raise Exception("The 'k' is not integer so the 'n' is wrong!")

    return int(_k)


if __name__ == '__main__':

    n = 7
    k= generate_k(n)
    print(k)
