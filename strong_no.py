#write a program to verify that the entered number is strong number or not.
#explaination x=145 =>  1!+4!+5!  => 1+24+120=145 

n=int(input('enter no: '))
sum=0
temp=n
while n>0:
    fact=1
    x=n%10
    for i in range(1,x+1):
        fact=fact*i
    sum=sum+fact
    n//=10
if temp==sum:
    print(f'{temp} is strong number')
else:
    print(f'{temp} is not a strong number')