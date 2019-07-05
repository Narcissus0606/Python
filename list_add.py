#list_1 + list_2的实现
def add_list(list_1,list_2):
    list = []
    for temp in list_1:
        list.append(temp)
    for temp in list_2:
        list.append(temp)
    return list

list_1 = [1,3,5]
list_2 = [2,3,6]
list = add_list(list_1,list_2)
print(list)
print("============================")
#实现list*n
def mult_list(list,n):
    result = []
    for i in range(0,n+1):
        for temp in list:
            result.append(temp)
    return result
list = [1,2,3]
print(mult_list(list,2))
        
str="123"
print(str[0:1].isalpha())
