# -*- coding:utf-8 -*-

import math
import cmath
import random

if __name__=="__main__":
    x = -100
    y = 1.9

    print(u"常用数学函数")
    print(abs(x))
    print(max(x, y))
    print(min(x, y))
    print(pow(y, 2))
    print(math.sqrt(y))

    print(u"常用随机函数")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(random.choice(a))
    print(random.randrange(2, 100, 5))
    print(random.random())

    print(u"常用三角函数")
    x = 100
    print(cmath.acos(x))
    print(cmath.cos(x))
    print(cmath.sin(x))

    print(u"数学常量")
    print(cmath.pi)