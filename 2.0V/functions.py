

def radian(value):
    value = value/57.3
    return round(value, 10)


def arctanx(num, str):
    tanx = num
    # 输入判断
    if(tanx >= -65535 and tanx <= 65535 and str == "弧度"):
        compute = True
    if(tanx >= -65535 and tanx <= 65535 and str == "角度"):
        compute = True
    else:
        compute = False
    # 符合输入规范则进行计算，并返回结果；否则返回"None"
    if(compute):
        # 反正切计算
        ret = 0
        get = tanx
        index = 1
        n = 0
        while index < 100000:
            index = index + 1
            ret = ret+(((-1)**n)/(2*n+1))*(get**(2*n+1))
            n = n + 1
        # ret = "%.3f" % ret
        if (str == "角度"):
            ret = ret / 3.1415926735 * 180
        #   print(tanx,"对应的反正切角度值arctanx为：",ret)
        if (str == "弧度"):
            ret = ret
        #   print(tanx,"对应的反正切弧度值arctanx为：",ret)
    else:
        ret = "None"
    return ret


def arcsine(float, str):
    # 输入正确性判断
    if(float >= -1 and float <= 1 and str == "弧度"):
        compute = True
    elif(float >= -1 and float <= 1 and str == "角度"):
        compute = True
    else:
        compute = False
    #
    # 符合输入规范则进行计算，并返回结果；否则返回"None"
    if(compute):
        # 反正弦计算
        res = float
        index = 1
        m = 2
        n = 1
        i = 1/2
        if(str == "弧度"):  # 结果输出采用弧度制
            while index < 197293:
                index = index + 2
                res = res + i*(float**index/index)
                m = m + 2
                n = n + 2
                i = i * n/m
            # res = "%.2f" % res
            # res = float(res)
        else:             # 结果输出采用角度制
            while index < 961337:
                index = index + 2
                res = res + i*(float**index/index)
                m = m + 2
                n = n + 2
                i = i * n/m
            res = res / 3.1415926535 * 180
            # res = "%.2f" % res
            # res = float(res)
        #
    else:
        res = "None"
    return res


class MyFun (object):
    def __init__(self, e=1e-3):
        self.e = e

    def cos(self, x):
        item = 1
        sum = 0
        i = 0
        f = 1
        while abs(item) > self.e:
            item = f * ((x ** i) / self . fact(i))
            sum += item
            f = - f
            i += 2

        return sum

    def fact(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i

        return result

    def sin(self, x):
        n = x
        sum,  i = 0,  1
        while abs(n) > self .e:
            sum += n
            i += 1
            n = - n * x * x / (2 * i - 1) / (2 * i - 2)

        return sum


def sin_t(x):
    pi = 3.1415926535
    cc = MyFun()
    return round(cc.sin(x*pi/180), 10)

# 计算cos


def cos_t(x):
    pi = 3.1415926535
    ss = MyFun()
    return round(ss.cos(x*pi/180), 10)


# 计算tan
def arcsine_t(x):
    return round(arcsine(x, "角度"), 10)


# 计算arctan
def arctan_t(x):
    return round(arctanx(x, "角度"), 10)
