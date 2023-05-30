import random as r

print('Guess number game.')
#Guessing number game

a=r.randint(0,10)
print(a)
print('You have only 5 attempts to play.')

for i in range(5,0,-1):
    no=int(input('Enter the number:- '))
    if no==a:
        print('YOU WON.')
    elif i-1 == 0:
        print('YOU LOST.')
    else:
        print(i-1,'attempts left.')
