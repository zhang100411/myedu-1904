#声明一个类 语法：class 类名（父类名)
class human(object):
    #_init_:类的初始化方法
    #self ：代表类的本身，name ， age ，sex的初始化的时候，要用到的参数
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

     #类中的方法， 必须包含self参数
    def eat(self):
        print(self.name+'在吃饭')

    def sleep(self):
        print(self.name+'在睡觉')

        #类中的方法，可以调用其他方法，可以调用属性，除了ini 方法
    def info(self):
        print('这个人是%s,今年%s岁,性别%s'%(self.name,self.age,self.sex))
        self.eat()

if __name__ == '__main__':
    #新建一个对象， 根据human类新建对象
    #对象是类的  实例化
    girl = human('天天',20,'男')
    #可以通过对象去调用类的方法和属性
    girl.eat()
    girl.sleep()
    girl.info()
    print(girl.name)