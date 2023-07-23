'''
map,filter and reduce
'''
#-------------------#
'''
def num_sqr(n):
    return n**2
numbers=range(1,11)
print(list(numbers))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(num_sqr,numbers)))#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
#--------------------#
'''
def num_even(n):
    if n%2==0:
        return n

numbers=range(1,11)
print(list(numbers))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(num_even,numbers)))#[2, 4, 6, 8, 10]
print(list(map(num_even,numbers)))#[None, 2, None, 4, None, 6, None, 8, None, 10]
'''

#-------------------#
'''
from functools import reduce

def summ(a,b):
    return a+b
numbers=range(1,11)
print(reduce(summ,numbers))#55
'''
#--------------------#

#with lambda:
'''
from functools import reduce
numbers=range(1,11)
result1=list(map(lambda x: x*2,numbers))
result2=list(filter(lambda x:x if(x%2==0) else(),numbers))
result3=reduce(lambda x ,y:(x+y),numbers)
print(result1)#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(result2)#[2, 4, 6, 8, 10]
print(result3)#55
'''
