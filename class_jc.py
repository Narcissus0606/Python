#父类、基类
class Person(object):
    def __init__(self,name,id_1):
        self.__name = name
        self.__id_1 = id_1
    def eat(self):
        print("Person eat!")
    def __str__(self):
        return "I'm a person!"

#子类、超类、派生类
class Student(Person):
    def eat(self):
        print("Student eat!")
    def __str__(self):
        return "I'm a student!"

class Teacher(Person):
    def eat(self):
        print("Teacher eat!")
    def __str__(self):
        return "I'm a teacher!"



xiaoming = Person("xiaoming",1)
stu_1 = Student("Peter",2)
tea_1 = Teacher("Any",3)
xiaoming.eat()
stu_1.eat()
tea_1.eat()
print(xiaoming)
print(stu_1)
print(tea_1)










