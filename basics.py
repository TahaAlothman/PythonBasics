##VARIABLE IN PYTHON
int ## for integer numbers ex : x = 2
##<class 'int'>

str ## for strings ex : 'ali' "Taha"
##<class 'str'>

float ## for float numbers ex: x = 5.2
##<class 'float'>

bool ## for bool (True/False) ex : x = False
##<class 'bool'>

list ##for list of values ex : x = [6,4,'ahmed',True]
##<class 'list'>

tuple ##for list of values ex : x = (3,4,6) {Elements in tuple sind const}
##<class 'tuple'>

dict ## for dict of values ex : x = {1: 'ali' , 2 :'amal'}
##<class 'dict'>
##type()  know the type of the Variable
##________________________________________##
x = 3
y = 'Taha'
print('x is',type(x),'y is',type(y))
 ##________________________________________##
h = (2)
print('h = (2)',type(h),'not tuple because just one Element')

## to generate a tuple from a single element
h = (2,)
print('h = (2,)',type(h))
##________________________________________##
print ('________________________________________')

##OPERATOR INTRODUCTION:
#ARITHMETIC OPERATORS
#COMPARISON OPERATORS
#ASSIGNMENTS OPERATORS


##ARITHMETIC OPERATORS:
print ('5 + 5 = ',5 + 5)
print ('7 - 5 = ',7 - 5)
print ('2 * 5 = ',2 * 5)
print ('5 / 4 = ',5 / 4)
print ('5 // 5 =',5 // 4)
print ('2 ** 3 =',2 ** 3)
print ('8 % 5 = ',8 % 5 )

print ('________________________________________')

#COMPARISON OPERATORS:
x = 2
y = 5

print ('x < y ?', x < y)
print ('x <= y ?', x <= y)
print ('x > y ?', x > y)
print ('x >=y ?', x >= y)
print ('x == 2 ?', x == 2)
print ('y != 5 ?', y != 5)

print ('________________________________________')

#ASSIGNMENTS OPERATORS:
a = 3
a += 1
print ('a = 3, a += 1 ===> a = ', a)

a = 2
a -= 1
print ('a = 2, a -= 1 ===> a = ', a)
a = 10
a *= 2
print ('a = 10, a *= 2 ===> a = ', a)
a = 6
a /= 2
print ('a = 6, a /= 2 ===> a = ', a)
a = 6
a //= 2
print ('a = 6, a //= 2 ===> a = ', a)

print ('________________________________________')

##_________________________________________________________##

#CONDITION:
x = 150

if x <150:
     print('x <150')
elif x > 150:
     print('x > 150')
else:
     print('x = ',x)

print ('________________________________________')


##_________________________________________________________##

username = 'admin'
password = 12345

if username == 'admin' and password == 12345:
    print (' welcome ')


else:
    print('username or password not correct')


print ('________________________________________')


##_________________________________________________________##

##true condition false

x = 2
print('x = 3') if x == 3 else print ('x != 3')


print ('________________________________________')

username = "Taha"
password = 12345

connection= True if username =="Taha" and password == 12345 else False
print(connection)

print ('________________________________________')
##_________________________________________________________##

##conditions Best Practices

Friends = ['Taha','Sami','Ali','Mohammed']

if 'Taha' in Friends:
    print ('Taha is my Friend')
else:
    print ('Taha is not my Friend')
    
print ('________________________________________')

##_________________________________________________________##


##any and all

x,y,z = 2,4,5

if all ([x ==2 , y==4 , z==5]):
    print(True)

if any ([x != 2 , y != 4, z != 5]):
    print (False)

print ('________________________________________')

##_________________________________________________________##
 ## Loop in Python : while or for

#while loop:

x = 1
while x <= 5:
    y = 1
    while y <= 10:
       print(f'{x} * {y} = ',x*y)
       y += 1
      
    x += 1
    print('- - - - - - - -')

print ('________________________________________')

##_________________________________________________________##

#for loop:

for x in (1,3,5,6,8,'Taha','Ali'):
    print(x)
print ('________________________________________')
## with rang(start,end,step)

print('even numbers between 2-50')
for x in range(2,52,2):# even numbers between 2-50
  
    print(x)
    

















 





