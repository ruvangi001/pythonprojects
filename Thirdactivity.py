#swap variable
#Swap the numbers with and without the 3rd Variable.

a=5
b=3
print('before swap:- ',a,b)
temp=a
a=b
b=temp
print('after swap:- ',a,b)

a=10
b=3
print('before swap:- ',a,b)
a=a+b
b=a-b
a=a-b
print('after swap:- ',a,b)

x=9
y=3
x,y=y,x
print(x,y)