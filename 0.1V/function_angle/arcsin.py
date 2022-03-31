from math import fabs
from math import pi

def asin(x):
    '''
    :param x: 输入参数为数值
    :return g 输出为角度值
    
    '''

    g = x
    t = x
    n = 1
    while (fabs(t) >= 1e-9):  #采用泰勒级数展开进行计算逼近函数值
        t = t * (2 * n - 1) * (2 * n - 1) * x * x / ((2 * n) * (2 * n + 1))
        n += 1
        g += t
    g = round(g / pi * 180, 1)
    return g
  
