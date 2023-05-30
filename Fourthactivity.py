#Fibonacci Series

no = int(input('Enter the length of fibonacci series:- '))
t=0;t1=1
if no==0:
    print('Enter positive integer.')
else:
    for i in range(0,no):
        print(t)
        t2=t+t1
        t=t1
        t1=t2

