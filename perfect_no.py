#write a program to verify that the entered number is perfect number or not.
#explaination i/p=6 factors= 1 2 3 6 , except its own factor sum the remaining factors (1+2+3=6) if i/p==o/p then its a perfect no.

n=int(input('enter no: '))
sum=0
for i in range(1,(n//2)+1):
    if n%i==0:
        sum=sum+i
if n==sum:
    print(f'{n} is perfect number')
else:
    print(f'{n} is not a perfect number')
