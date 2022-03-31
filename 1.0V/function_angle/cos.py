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


def cos(x, flag=False):
    """
    输入值 角度或者弧度
    flag:Ture 表示弧度，False 表示角度 默认角度
    return cosx 保留小数后三位
    """
    if not flag:
        x = x / 180 * math.pi
    # 根据周期性，对弧度划分到[0,2*pi]
    if x < 0 or x > 2 * pi:
        x = x % (2 * pi)

    return round(taylor(x, 50), 3)


if __name__ == "__main__":
    test = cos(60)
    print(test)
