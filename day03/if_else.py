
def if_mode():
    #  根据表达式 决定 a 是 True 还是 Flase
    a = 9>8
    # a 是 True，所以条件成立 打印 a 是True
    # 如果a 是 Flase 条件不成立 走else 分支 ， 打印a 是Flase
    if a :
        print('a 是 True')
    else :
        print('a 是 Flase')
def else_demo():
    a=5
#     =是赋值 ， ==是 判断相等
    if a == 1:#判断 a是否等于1
        print('a是1')
    elif a == 2:#判断 a是否等于2
        print('a 是 2')
    elif a == 3:#判断 a是否等于3
        print('a 是 3')
    elif a ==4:#判断 a是否等于4
        print('a 是 4')
    else :
        print('a 不是1,2,3,4')

if __name__ == '__main__':
    # if_mode()
    else_demo()