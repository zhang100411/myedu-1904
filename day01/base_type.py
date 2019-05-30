
a = 5
# def:声明方法的关键字;int_demo：方法的名字（）：下面写方法的内容
def int_demo():
    # 声明一个变量=前面是变量名 aint，=后面是变量值，int类型的5
    aint = 5

    # type(aint): 获取aint的数据类型（变量类型），print：打印出他的类型
    print(type(aint))

def str_demo():
    # 声明一个变量=前面是变量名 aint，=后面是变量值，str类型的5
    astr ='5'

    # type(astr): 获取astr的数据类型（变量类型），print：打印出他的类型
    print(type(astr))
#这是一个main方法，可以直接执行，main方法下面不能再有其他方法
def float_demo():
    afloat=1.1
    print(a)
    print(type(afloat))
def type_zhuanhuan():
    b = '100'
    #将b的类型转换成a
    b = int(b)
    print(type(b))
# 字符串拼接
def str_join():
    a = 123
    b = '哈哈哈'
    c = '你好'
    #如果两个变量都是字符串，直接用+连接
    print(b+c)

    #如果有其他类型，第一种：需要用str（）方法转换成str类型才能用+连接
    print(str(a)+b+c)

    #第二种：%s:这个是占位符
    print('a是%s,b是%s,c是%s'%(a,b,c))

# 方法中括号的东西叫参数,多个参数用,分隔开
def add(num1,num2):
    print(num1)
    print(num2)
    print(num1+num2)
    #方法执行到return 就返回return后面的内容
    return num1+num2
if __name__ == '__main__':
    # int_demo()
    # str_demo()
    # float_demo()
    # type_zhuanhuan()
    # str_join()没有返回值, 所以a的值就是none
    a =str_join()
    # add(10,40)有返回值，所以b的值就是50
    b =add(10,40)
    print('----------')
    print(a)
    print(b)
    print(type(a))
