from math import fabs
from math import pi


def sin(x, flag=False):
    """
    输入 x
    flag Ture 弧度 ，False 角度 默认角度
    """
    if not flag:
        x = x / 180 * pi  # 输入角度转换为弧度

    # 根据周期性，对弧度平移到[0,2*pi]
    if x < 0 or x > 2 * pi:
        x = x % (2 * pi)
    g = 0
    t = x
    n = 1

    # 使用泰勒展开式对sin值进行计算
    while (abs(t) >= 1e-15):
        # 设置计算的精度
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return round(g, 3)  # 计算结果保留三位小数


# test
if __name__ == "__main__":
    ans = sin(-45)
    print(ans)
