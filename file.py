"""
文件定义
1.文件读写
    参数 1：路径（相对或绝对）
    参数 2：打开方式
    open完成之后必须使用对象接受
    文件使用完后，必须要关闭，必须释放资源
    读取全部文件内容(readlines)
    按行读取文件(readline)
2.文件异常处理
"""
"""
file = open("C:\\Users\\Narcissus\\Desktop\\0705.txt","r")
print(file.readlines())
file.close()

#使用这个with上下文，就可以不用再关闭文件了
def read_file():
    try:
        with open("C:\\Users\\Narcissus\\Desktop\\0705.txt","r") as f:
            data = f.readline()
            while data != None and data != "":
                print(data)
                data = f.readline()
    except Exception as e:
        print(e)

read_file()
"""
list = [0,1,2]
print(len(list))
print(list[0])








