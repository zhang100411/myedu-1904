def for_demo():
    #for(关键字) i（变量名，代表循环次数） in（关键字） range（迭代器函数）
    for i in range (6):
        print('Hello World')
        print(i)

def for_demo1():
    #for(关键字) i（变量名，代表循环次数） in（关键字） range（迭代器函数）
    #两个参数时： 从第一个参数开始计数，到第二个参数的前一位 停止
    for i in range (6,11):
        print('Hello World')
        print(i)

def for_demo2():
    #三个参数时：从第一个参数开始计数，到第二个参数的前一位 停止。 每次循环 递增 参数三（步长）
    for i in range (6,11,2):
        print(i)

        #当步长为负数时，第一个参数 要比第二个参数 大
    for i in range (20,8,-3):
         print(i)

#遍历 list
def for_list():
    blist = ['哈','喽','wo','de',1,2,3]
    #方式一
    for i in blist:
        print(i)
    #方式二
    for i in range(len(blist)):
        print(blist[i])

#嵌套循环
def for_for():
    # end ='xxx' :让print 以什么结尾
    #/n ：就是换行符
    #print 默认 以换行符结尾
    for i in range(5):
        print('你好')
        for j in range(2):
            print('世界',end=',')

def break_continue():
    for i in range(5):
        print(i)
        if i ==2 :
            break

    for i in range(5):
        if i ==2 :
            continue
        print(i)


if __name__ == '__main__':
    # for_demo2()
    # for_list()
    # for_for()
    break_continue()