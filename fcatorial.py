# 1)write a program to find a factorial of a number.

n=int(input('enter no: '))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f'factorial of {n} is {fact} ')


# 2)write a program to find factors of a given number.

n=int(input('enter no: '))
print(f'factors of the given number {n} are:')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
