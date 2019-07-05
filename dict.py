"""
dict字典
字典相当于Java map
key value组成
dict = {"key":value}

定位元素
    value = dict["key"]
    for key in dict

增，删，改，查
"""
dict = {123:456}
key_1 = "apple"
value = "mac pro"
dict[key_1] = value
#获取value
print(dict["apple"])
print(dict[123])

for key in dict:
    print(key,"->",dict[key])
print("=========================")    
#增
dict["123"] = 456
dict.update(b=123)
#update函数如果有，就将value更新；如果没有key，那么就添加一条
print(dict)
print("=========================") 
#删(del,pop,clear,remove)









