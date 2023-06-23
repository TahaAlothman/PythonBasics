'''
class A:
    def do(self):
        print('class A')

class B(A):
    pass

class C:
    def do(self):
        print('class c')
    def sum(self,x,y):
        print(f'{x} + {y} =',x+y)
class D(B,C):
    pass

c1=D()
c1.do()
c1.sum(3,5)       ##==> class A    3 + 5 = 8
              
print(D.mro())     ##==>"um den Pfad zu erkenne"     [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]


print('--------------------------------------------------------------------')

'''
#____________________________________________________________________________#
'''
class Student:
    def __init__(self,name):
        print(f'welcome {name}')
        self.marks=[]


    def add_mark(self,mark):
         self.marks.append(mark)
         print(self.marks)

         
    def get_avg(self):
        avg= sum(self.marks)/len(self.marks)
        print(avg)
        




c=Student('Taha')
c.add_mark(40)
c.add_mark(50)
c.add_mark(30)
c.get_avg()




===============
#output:
'''


'''
welcome Taha
[40]
[40, 50]
[40, 50, 30]
40.0
'''
#____________________________________________________________________________#

'''
bank
    - creat account: name, age , gender
    - desposite
    - withdrow
    - view balance
    - show all details
'''

'''
class User:
    def __init__(self,name,age,gender):
        print(f'welcome {name}')
      
        self.name=name
        self.age=age
        self.gender=gender
    def client_datails(self):
        print(f'Name : {self.name}\nAge : {self.age}\nGender : {self.gender}\nBalance : {self.balance}')

    
class Bank(User):
    def __init__(self,name,age,gender):
          self.balance=0
          super().__init__(name,age,gender)
    def deposite(self,amount):
        self.balance += amount
        print(f'you current balamce : {self.balance}')

    def withdrow(self,amount):
        if amount > self.balance:
            print('not enouph balance')
            return
        self.balance -=amount
        print(f'you current balamce : {self.balance}')

    def view_balance(self):
         print(f'you current balance : {self.balance}')


    
x=Bank('ali',30,'male')

x.deposite(100)

x.deposite(100)

x.withdrow(123)


x.view_balance()
x.client_datails()

'''
#____________________________________________________________________________#
'''
kurs :

    - Anmelden (name,age,adresse,nummer)
    -Thema ()
    -dauer
    -kosten

'''
























    
