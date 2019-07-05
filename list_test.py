list_1 = []
#这相当于一个空的列表 []代表是一个列表的含义
print(list_1)
var1 = "zs"
var2 = "list"
var3 = "ww"
#通过赋值的方式给列表进行初始化
list_1 = [var1,var2,var3]
print(list_1)
list_1 = [var1,var2,var3,False,1,123]
print(list_1)
list_2 = [list_1,var3,var2]
"""
锁定下标
从0开始计算
序列
for i in list:
按照下标进行获取
获取数据和遍历数据
"""
print("=========================")
for temp in list_2:
    print(temp)
print("=========================")
"""
增：
    append方式，在list列表后面插入
    insert方式，list.insert(位置，数据）
删：
    list.remove(obj)
    pop(index)参数就会固定位置被删除
    del是内存空间位置全部清除，python中允许程序员自己清除多余数据
改：
    定位元素并进行数据修改
"""
list_3 = list_1 + list_2
print(list_3)






















