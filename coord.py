class Line:
    def __init__(self,coeffi:list[int|float]):
        '''
        记录曲线
        coeffi:各项的系数，由低次项到高次项
        '''
        if len(coeffi) == 0:
            raise ValueError('Line对象初始化时至少输入一个数字')
        for each in coeffi:
            if not isinstance(each,(float,int)):
                raise TypeError('Line对象只能接受数字')
        while len(coeffi) > 1 and coeffi[-1] == 0:
            coeffi = coeffi[:-1]
        self.coeffi = list(coeffi)
        self.max = len(coeffi) - 1#记录最高次项

    def __str__(self) -> str:
        export = f'{self.coeffi[0]}'
        for each in enumerate(self.coeffi):
            if each[1] == 0:
                continue
            if each[0] == 0:
                continue
            elif each[0] == 1:
                export = f'{each[1]} * x + ' + export
                continue
            export = f'{each[1]} * (x^{each[0]}) + ' + export
        export = 'y= ' + export
        return export
    __repr__ = __str__

    def __call__(self,num:float) -> float:
        '''返回曲线在x对应的值'''
        export = 0
        for each in enumerate(self.coeffi):
            export += each[1] * (num ** each[0])
        return export
    
    def __add__(self,line):
        if line.max > self.max:
            self,line = line,self
        export = list()
        for each in enumerate(self.coeffi):
            try:
                export.append(each[1] + line.coeffi[each[0]])
            except IndexError:
                export.append(each[1])
        return Line(export)
    
    def __sub__(self,line):
        return self + (-line)
    
    def __neg__(self):
        export = [-i for i in self.coeffi]
        return Line(export)
    
    def __mul__(self,other):
        if isinstance(other,(int,float)):
            export = list(map(lambda x:x * other,self.coeffi))
            return Line(export)
        elif isinstance(other,Line):
            export = [0] * (len(self.coeffi) + len(other.coeffi) - 1)
            for each in enumerate(self.coeffi):
                for each1 in enumerate(other.coeffi):
                    export[each[0] + each1[0]] += each[1] * each1[1]
            return Line(export)
        else:
            raise ValueError(f'曲线不能和{type(other)}相乘')
        
    def __truediv__(self,other):
        if isinstance(other,(int,float)):
            export = list(map(lambda x:x / other,self.coeffi))
            return Line(export)
        else:
            raise ValueError('sorry,这部分功能还没有实现')
    
def lagrange_inter(point:list[tuple[float]]):
    '''
    拉格朗日插值法求曲线
    point:待插值的点
    '''
    cpy_point = point.copy()
    export = Line([0])
    for each in point:
        cpy_point.remove(each)
        base = Line([each[1]])#插值基函数
        for point in cpy_point:
            if each[0] == point[0]:
                raise ValueError('拉格朗日插值法不能有相同的x值')
            base *= Line([-point[0],1])
            base /= each[0] - point[0]
        export += base
        cpy_point.append(each)
    return export

if __name__ == '__main__':
    points = [(2,6),(3,6),(4,18),(5,30),
              (6,66),(7,126),(8,258),(9,510),(10,1026),
              (11,2046),(12,4098),(13,8190),(14,16386),
              (15,32766),(16,65538),(17,131070),(18,262146),
              (19,524286),(20,1048578),(21,2097150)]
    point = [(1,2),(2,4),(3,6)]
    line1 = Line([1,1])
    line2 = Line([1])
    print(lagrange_inter(point))
