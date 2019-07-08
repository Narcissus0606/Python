class Person(object):
    head = 1
    foot = 2
    def __init__(self):
        print("tounihouzi")
        self.head = 3
        self.foot = 6
    def run(self):
        print(self)
    def learn(self,abc):
        print(abc)
    def pro(self):
        print(self.head,self.foot)

p = Person()
#print(p)
#p.run()
#p.learn("123")
#p._init_()    
p.pro()
