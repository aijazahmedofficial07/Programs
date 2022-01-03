#write a program to verify that the entered number is neon number or not.

n=int(input('enter no:'))
x=0
sqr=n*n
while sqr>0:
    r=sqr%10
    x+=r
    sqr//=10
if x==n:
    print(f'{n} is a neon number')
else:
    print(f'{n} is not a neon number')