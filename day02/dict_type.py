import json
#字典 以{ }包起来，:前面是key ，后面是value;多个键值对用,分隔开
adict ={'username':"亚索","password":"123456"}

 # 字典是无序的，他没有索引，只能通过key 去访问value，并且key不能重复
def dict_sel():
    print(adict['username'])
# 更新字典里的 value
def dict_update():
#     通过key去修改 value
    adict['username']='zhj'
    print(adict)
# 删除字典里的键值对
def dict_tel():
    adict.pop('username')
    print(adict)
#     增加字典里的键值对
def dict_add():
    # 如果key 在原本字典中 不存在，则会新加一个键值对
    adict['age'] = 25
    print(adict)
    # 合并方式一：将bdict添加进adict
    bdict = {'list':[1,2,3],'tuple':[4,5]}
    adict.update(bdict)
    print(adict)
     # 合并方式二：将adict和bdict合并，并新生成一个ddict  注意第二个字典参数前要加 2个**
    cdict = {"password":"654321",'class':'1994'}
    ddict = dict(adict,**cdict)
    print(ddict)

def dict_zhuanhuan():
    print(type(adict))
    #josn.dumps(admin)字典 转换成 字符串 ,ensure_ascii = False 防止乱码
    str_dict = json.dumps(adict,ensure_ascii=False)
    print(str_dict)
    print(type(str_dict))

    dict_str='{"username":"亚索","password":"123456"}'
#     json.loads(dict_str) 字符串 转换 成字典
    json_loads= json.loads(dict_str)
    print(type(json_loads))
# 题;新建一个字典变量，里面有2个键值对，通过key访问一个值，删除一个键值对，添加一个键值对，更改任意一个值，在新建一个字典，将两个合并
def home_work():
    adict = {'username': "abcd", "password": "1234"}
    print(adict['username'])
    adict.pop('username')
    adict ['age'] = 5
    bdict = {"username":"亚索","password":"123456"}
    cdict = dict(adict,**bdict)
    print(cdict)


if __name__ == '__main__':
    # dict_sel()
    # dict_update()
    # print(dict_tel())
    # dict_add()
    # dict_zhuanhuan()
    home_work()
