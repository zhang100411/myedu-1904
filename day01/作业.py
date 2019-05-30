# 导入模块
from day01 import base_type
def def1():
    print('def1')

def def2():
    print('def2')

def def3():
    print('def3')
if __name__ == '__main__':
# 使用其他模块的方法：语法 模块名.方法名()
#  给指定参数入参，指定num2=55 ，指定num1 =45
#     value =base_type.add(num2=55, num1=45)
#  默认参数入参，就是按照参数的顺序入参，55是num1,45是num2
#    value =base_type.add(55, 45)
#     print(value)
#     print(type(str(value)))
    a ='真假奥迪啥都物资'
    # 切片演示
    print(a[2:])
    print(a[3:5])
    # 根据索引取值演示
    print(a[-2])
    print(a[2])
    # 反转
    print(a[::-1])