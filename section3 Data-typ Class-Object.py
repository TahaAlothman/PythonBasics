#string Methode

text = 'my Name is Taha , i am Python developer'
text = text.upper() 
print(text)                 #MY NAME IS TAHA , I AM PYTHON DEVELOPER
text =text.lower()          
print(text)                 #my name is taha , i am python developer
text = text.title()
print(text)                 #My Name Is Taha , I Am Python Developer     
text = text.replace('Python' ,'java')
print(text)                 #My Name Is Taha , I Am java Developer
'''text =text.split(',')
print(text)'''              #['My Name Is Taha ', ' I Am java Developer']

print(text[-2])             #e
print(text[0:7])            #My Name
print(text[:7])             #My Name
print(text[7:])             #Is Taha , I Am java Developer

#List Mehtode

l=[0,1,2,3,True,False,'welcome']

l.append(1000)
for x in l:
    print(x)               #[1,2,3,True,False,'welcome',1000]
print ('---------------------------------')
l.insert(3,33)

for x in l:
    print(x)               #[1,2,3,33,True,False,'welcome',1000]
print ('---------------------------------')    
l.remove(False)
for x in l:
    print(x)               #[1,2,3,3,33,True,'welcome',1000]
print ('--****-------------------------------')
l=[23,45,1,2,6,8]
l.sort()
for x in l:                #[1,2,6,8,23,45]
    print(x) 
print ('---------------------------------')

l.reverse()

for x in l:                #[45,23,8,6,2,1]
    print(x) 
print ('---------------------------------')
l=[2,3,6,1,0,5,4,3,7]
l.sort(reverse=True)
for x in l:                #[7,6,5,4,3,3,2,1,0]
    print(x) 
print ('---------------------------------')
l.pop()

for x in l:                #[7,6,5,4,3,3,2,1]
    print(x) 
print ('---------------------------------')



#tuple

t=(1,2,3,4,True,23,0)
print(min(t))               #0
print(max(t))               #23

print ('---------------------------------')



#dict

d={'ali':70 , 'mahmoud':80 ,'Taha':44 }

print(d['ali'])           #70

for x in d:
    print(x)             #ali  mahmoud  Taha   (for x in d = for x in d.keys()..)


for x in d.values():    #70    80   44
    print(x)


for x,y in d.items():      # ali 70    mahmoud 80    Taha 44
    print(x,y)


print ('--------------------------------------------')


#class and object:



class Calculator:
    def sum(self,x,y):   #self like this in java (Location in memory Reservation for an object)
        print(x+y)
    def __init__ (self,name,age):  #constructor
        print (f'welcom {name} you are {age} years old')


c1= Calculator('Taha',32)   #welcom Taha you are 32 years old
c1.sum(10,3)                # 13

print ('--------------------------------------------')



class Calculator1:
    def sum(self,x,y):
        print(x+y)
    def __init__ (self,name,age):  #constructor
        print (f'welcom {name} you are {age} years old')

class SciCale(Calculator1):
    def sum(self,x,y):
        print('x + y =',x+y)
    def mul(self,x,y):
        print(x*y)



c2= SciCale('Taha',32)       #welcom Taha you are 32 years old
c2.mul(9,3)                  #27
c2.sum(1,4)                  #x + y = 5

'''

encapsulation : self
inheritance   : erben
polymorphism  : vielfachheit
abstraction   :

'''
