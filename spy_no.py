#write a program to verify that the entered number is spy number or not.

n=int(input('enter no:'))
sum=0
p=1
temp=n
while n>0:
    r=n%10
    sum+=r
    p*=r
    n//=10
if sum==p:
    print(f'the sum and product of {temp} is {p} and its a spy number')
else:
    print(f'the sum and product of {temp} is {p} and its not a spy number')