'''
 - start : welcome message , game Option
 - enter game number
 - option : option to exit
 - start play game
 - finish game : play again
 - yes : play again - no : exit
'''
class Game:
    def __init__(self,name):
        while True:
            print(f'Hallo {name} Welcome in our Game :)')
            print("choose one of these number:\n1:if you want play Names\n2:if want play Numbers\n3:if you don't want play")

            user_input=int(input('Enter a Number please:\n'))
            if user_input == 3:
                break
            elif user_input ==1:
                self.Names()
            elif user_input ==2:
                self.Numbers()
            else:
                print('Please write one of the above numbers')
        
            inputs=input("press any key to play again,'n' to exit ;)")
            if inputs == 'n':
                 break


        
    def Names(self):
        names= input('Enter the Names please : ')
        names= names.split(',')
        length= int(input('Enter the Length please:'))
        for x in names:
            if len(x) > length:
                print(x)
    def Numbers(self):
        start=int(input('Enter the First Number please : '))
        end=int(input('Enter the last Number please : '))
        even=[]
        odd=[]
        for x in range(start,end+1):
            if x % 2 ==0:
                even.append(x)
            
            else:
                odd.append(x)
        print(even)
        print(odd)




x=Game('Taha')

        









        

















































