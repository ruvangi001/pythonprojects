import random as r
a=input('Enter the rock-paper-scissor game:- ')
print(a)

l=['rock','paper','scissor']
b=r.choice(l)
print(b)

if a==b:
    print('Draw')
elif a=='rock' and b=='scissor':
    print('You won')
elif a=='paper' and b=='rock':
    print('You won')
elif a=='scissor' and b=='paper':
    print('You won')
else:
    print('You Lost')