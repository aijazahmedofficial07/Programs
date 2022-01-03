#write a program to verify that the entered number is special number or not.

n=int(input('enter no:'))
x=0
temp=n
p=1
while n>0:
    r=n%10
    x+=r
    p*=r
    n//=10
if (x+p)==temp:
    print(f'{temp} is a special number')
else:
    print(f'{temp} is not a special number')