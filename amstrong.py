#write a program to check entered number is amstrong or not.

n=int(input('enter no: '))
p=0
sum=0
temp=n
while temp>0:
    p+=1
    temp//=10
temp=n
while temp>0:
    r=temp%10
    sum=sum+(r**p)
    temp//=10
if sum==n:
    print(f'{n} is an Amstrong number')
else:
    print(f'{n} is not an Amstrong number')