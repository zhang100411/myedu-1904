# 这就是一个列表的数据类型,英文 是 list, 也叫 数组
alist = ['是打发',2,'你好',6,7,1,3]

# 访问list
def list_sel():
    # 通过索引访问: 从0开始数
    print(alist[0])
# 访问倒数第三位：倒序取值，从-1开始数
    print(alist[-3])
#     通过切片访问，语法：前索引值:后索引值 取得时候取到后索引值的前一位
    print(alist[2:3])
#     访问 从第五个开始到后面的所有
    print(alist[4:])
#     不填值的话，从第一个开始取值
    print(alist[:4])
#     调用删除方法，填写参数:索引值 就可以删除指定元素,并把删除的元素返回回来,赋值给a
    a = alist.pop(6)
    print(alist)
    print(a)

def list_add():
    blist = [1,2,3,'4']
#     增加元素，增加在末尾
    blist.append('世界')
    print(blist.append)
    clist =[9,8,7,'你好']
    # blist.append(clist)
    # 合并两个list 中的元素
    blist.extend(clist)
    print(blist)
def list_update():
    qlist=[0,1,2,3,4,5,6]
#     更新列表中的元素，根据索引进行更新，值写在=的后面就行
    qlist[1]=688
    print(qlist)
#     更新第三位，改为200
    qlist[2]=200
    print(qlist)
def list_order_by():
    # 从小到大排序
    qlist = [1,2,3,4,6,5]
    qlist.sort()
    print(qlist)
#     从大到小排序
    qlist.sort(reverse=True)
    print(qlist)
def list_distinct():
    # set(vlist):使用set方法对list进行去重，去重后不是list类型，用list（）方法将这个数据转换为list类型
    vlist = [1,2,2,3,3,4,5,6,6]
    vlist = list(set(vlist))
    print(vlist)
    print(type(vlist))
def list_len():
    # len():获取列表的长度，有几个元素，返回几个元素
    vlist =[1,2,3,4,5]
    print(len(vlist))
def list_work():
    llist = [1,2,3,4,5]
    print(llist[2])
    print(llist[1:4])
    llist.pop(3)
    mlist=[4,5]
    llist.extend(mlist)
    llist[0] = '5'
    print(len(llist))
    print(llist)

if __name__ == '__main__':
    # list_sel()
    # list_add()
    # list_update()
    # list_order_by()
    # list_distinct()
    # list_len()
    list_work()