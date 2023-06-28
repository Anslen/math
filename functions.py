def primeFactor(num,mul:bool = False)->list:
    '''
    num:需要分解的数
    mul:是否转换为乘法格式
    '''
    try:
        num = int(num)#尝试转化为整数
    except ValueError:
        raise ValueError('请输入一个数字')
    if num <= 0:
        raise ValueError(f'请输入大于等于1的数字,{num}')
    if num == 1:#遇到1直接输出1
        return [1]
    result = []#存放结果
    notResult = 1#最大的不是因数的数
    while num != 1:#num不为1时持续进行枚举
        for i in range(notResult+1,num+1):#判断每一个数字是否为因数
            if num % i == 0:#可以整除
                result.append(i)
                num = num // i#i加入结果后将num除以i
                break
            else:
                notResult = i#不能整除时放入notResult下次直接跳过
    if mul:
        result = [str(i) for i in result]
        return '*'.join(result)
    return result

def maxFactor(x,y):
    '''
    求x,y的最大公因数
    '''
    factor_x = primeFactor(x)
    factor_y = primeFactor(y)
    export = 1
    for each in factor_y:
        if each in factor_x:
            factor_x.remove(each)
            export *= each
    return export

if __name__ == '__main__':
    print(maxFactor(840,1764))