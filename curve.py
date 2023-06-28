import numpy as np

class Curve:
    __slots__ = ['func']
    def __init__(self,func):
        '''曲线类   func:输入x对输出y的函数'''
        self.func = func

    def __add__(self,other):
        if type(other) is not Curve:
            raise TypeError(f'曲线不能与{type(other)}相加')
        def new(num):
            return self.func(num) + other.func(num)
        return Curve(new)

    def __sub__(self,other):
        if type(other) is not Curve:
            raise TypeError(f'曲线不能与{type(other)}相减')
        def new(num):
            return self.func(num) - other.func(num)
        return Curve(new)
    
    def __mul__(self,other):
        if type(other) is not Curve:
            raise TypeError(f'曲线不能与{type(other)}相乘')
        def new(num):
            return self.func(num) * other.func(num)
        return Curve(new)
    
    def __truediv__(self,other):
        if type(other) is not Curve:
            raise TypeError(f'曲线不能与{type(other)}相除')
        def new(num):
            if other(num) == 0:
                return np.nan
            return self.func(num) / other.func(num)
        return Curve(new)
    
    def __pow__(self,other):
        if type(other) is Curve:
            def new(num):
                return self.func(num) ** other.func(num)
            return Curve(new)
        try:
            1 ** other
            def new(num):
                return self.func(num) ** other
        except:
            raise TypeError(f'不能对{type(other)}求平方')

    def __call__(self,num):
        return self.func(num)
    
if __name__ == '__main__':
    f = Curve(lambda x:x ** 2)
    g = Curve(lambda x: 2*x)
    h = f + g
    print(h(5))
