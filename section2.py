#Loop with List :

List = [[1,2,4],[5,7,8],[3,9]]


for x in List:
    print (x) 
print('__________________')

for x in List:
    for y in x:
        print(y)
print('__________________')
for x in List[0]:
       print(x)

print('__________________') 
#________________________________________________________#

#Loop Control Statements

#Break Statements

for x in range (10):
    if x == 6 :
        break
    print (x)

print('__________________')

#Continue Statement

for x in range (10):
    if x == 6 :
        continue
    print (x)

print('__________________')


#________________________________________________________#

#pass

for x in range(10):
    pass


print('__________________')


#________________________________________________________#

#Loops Best Practices:Example 1

print ('Number\tSquare')

print('---------------')

for x in range (1,11):
    print (f'{x}\t{x*x}')


print('__________________')


##User enters the values
'''start = int (input('Enter start :'))
end  =  int (input('Enter end :'))

print ('Number\tSquare')

print('---------------')

for x in range (start,end+1):
    print (x,'\t',x*x)


print('__________________')'''

##stern

'''start = int (input('Enter start :'))
end  =  int (input('Enter end :'))

for x in range(start):
    print('*'*end)'''



for x in range (1,9):
    print('*'*x)




print('__________________')


##________________________________________________________#

##Function

'''
print("Write all numbers between 1-1000 that are divisible by 2 numbers that entered by user")

def my_funktion ():
    x = int (input('Enter first Number : '))
    y = int (input ('Enter second Number :'))
    for a in range(1,1001):
        if a % x == 0 and a % y == 0:
            print(a)
my_funktion ()



print('__________________')

'''
##________________________________________________________#

'''

def my_sum ():
    x = int (input('Enter first Number : '))
    y = int (input ('Enter second Number :'))
    return x+y
x = my_sum ()
print(x)


print('__________________')

'''
##Parameters and Arguments in Function:
#1.required: Parameter is important,the function without it gives error. ex:
'''
def mysum(x,y):
return x+y

x = mysum(5)
print(x)

(====> error:missing required positional argument:'y')
'''
#2.keyword: Parameter position change. ex :
'''
ef mysum(x,y):
return x+y

x = mysum(y=3, x=4)
print(x)
'''

#3.default : wihtout parameters. ex:
'''
def mysum(x,y):
return x+y

x = mysum()
print(x)

(====> error:missing 2 required positional argument: 'x' and 'y')

def mysum(x=0 ,y=0):
return x+y

x = mysum()
print(x)

(=====> output :  0)


def mysum(x=0 ,y=0):
return x+y

x = mysum(6)
print(x)

(=====> output :  6)
'''

##lambda function: return automatich:
mysum = lambda x,y : x +y

print(mysum(2,4))


print('__________________')




##________________________________________________________#

#scope:
f = 0
print(f) # 5


def do():
    global f
    f = 5 # local
    print (f) # 5

do()

print(f) #5 _____ wihtout global in do() output===> 0 5 0














