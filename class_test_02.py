class A(object):
    def __init__(self,name,id_1):
        self.__name = name
        self.__id_1 = id_1
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_id(self):
        return self.__id_1
    def set_id(self,id_1):
        self.__id_1 = id_1


a = A("Peter",1)
#当前这个a对象是否能够拿到name，id_1
"""
print(a.name)
print(a.id_1)
a.name = "45454"
a.id_1 = 3456
print(a.name)
print(a.id_1)
"""
a.set_name("Tim")
print(a.get_name())
a.set_id(2)
print(a.get_id())
