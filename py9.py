import random
x=random.randint(1,9)
count=0

while(True):

    guess=int(input('Guess any no. between 1 and 9:'))
    
    if(guess==x):
        print('correct')
        count=count+1
    elif(guess<x):
        print('too low')
        count=count+1
    else:
        print('too high')
        count=count+1

    end=input('enter exit to end the game/press enter key to continue:')    
    if(end=='exit'):
        print('count=',count)
        break
  

