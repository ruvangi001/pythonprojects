# Write a code in python in which you can get “Fizz Buzz” for all numbers which can be divided by (3, 5, 15). The range should from (1 to 100).

#----FizzBuzz game-------
l=[]
for i in range(1,101):
    if i%15==0:
        a='fizzbuz'
        l.append(a)
    elif i%5==0:
        b='buzz'
        l.append(b)
    elif i%3==0:
        c='fizz'
        l.append(c)
    else:
        l.append(i)
print(l)


