from functions import primeFactor
from functools import reduce
from fractions import Fraction

class Root():
    def __init__(self,num = 0,k = 1):
        '''num:根号下的值
           k:系数'''
        self.num = num
        self.k = k
        self.simple()
        self.value()
    
    def value(self):
        '''获取数值，是整数转为整形'''
        value = self.k * pow(self.num,0.5)
        if int(value) == value:
            self.value = int(value)
        else:
            self.value = value
            
    def simple(self):
        '''化简根式'''
        factor = primeFactor(self.num)#分解质因数
        i = 0
        while i < len(factor):#遍历每个质因数
            arg = factor[i]
            if factor.count(arg) > 1:#两个相同质因数
                factor.remove(arg)
                factor.remove(arg)
                self.k *= arg
            else:
                i += 1
        if factor:#计算新的num值
            newnum = reduce(lambda a,b:a*b,factor)
        else:
            newnum = 1
        self.num = newnum
        
    def __repr__(self):
        if self.num == 1:#省略根号1
            return str(self.k)
        if self.k == 1:#省略'1*'
            return(f'根号{self.num}')
        return(f'({self.k})*根号({self.num})')
        
    __str__ = __repr__
    
    def __mul__(self,other):
        if isinstance(other,(int,Fraction)):
            return Root(self.num,self.k*other)
        if isinstance(other,Root):
            return Root(self.num * other.num,self.k * other.k)
        raise ValueError('输入的值不正确')

    def __rmul__(self,other):
        return self*other

    def __truediv__(self,other):
        if isinstance(other,(int,float,Fraction)):
            return Root(self.num,self.k*other)
        if isinstance(other,Root):
            a = self
            b = other
            a.num *= b.num
            b.num *= b.num
            a.simple()
            b.simple()
            k = Fraction(a.k,b.k)
            a.k = k.numerator
            if k.denominator == 1:
                return a
            b.k = k.denominator
            if a.num == 1:
                return Fraction(a.k,b.k)
            return f'Fraction({a},{b})'

    def __rtruediv__(self,other):
        if isinstance(other,(int,float)):
            other = Root(1,other)
        if isinstance(other,Fraction):
            self.k *= other.denominator
            other = other.numerator
        return other/self
if __name__ == '__main__':
    print(Root(15135454687541))