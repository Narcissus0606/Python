class Anminal(object):
    def print_type(self,t):
        print(type(t))
        
class Person(Anminal,object):
    pass

class Worker:
    pass

class Student(Person,Worker):
    pass



p = Person()
w = Worker()
s = Student()
print(type(s))
