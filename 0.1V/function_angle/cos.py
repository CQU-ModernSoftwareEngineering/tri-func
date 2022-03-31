import math
from math import pi


def factorial(a):
    """
    阶乘
    """
    b = 1
    while a != 1:
        b *= a
        a -= 1
    return b


def taylor(x, n):
    a = 1
    count = 1
    for k in range(1, n):
        if count % 2 != 0:
            a -= (x ** (2 * k)) / factorial(2 * k)
        else:
            a += (x ** (2 * k)) / factorial(2 * k)
        count += 1
    return a


def cos(x):
    """
    输入值x
    返回cos值
    """
    x = x / 180 * math.pi

    return round(taylor(x, 50), 3)


if __name__ == "__main__":
    test = cos(60)
    print(test)
