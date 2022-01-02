#1) if a)I/P= 123 ,O/P= even count=1,odd count=2. b)I/P=2560 , O/P= even count=2,odd count=1,zeros count=1. number of odd, even, zeros elemet in ithe given input.

n=int(input('enter no: '))
ec=0
oc=0
zc=0
while n>0:
    x=n%10
    if x!=0:
        if x%2==0:
            ec+=1
        else:
            oc+=1
    else:
        zc+=1
    n//=10
print(f'even count={ec}')
print(f'odd count={oc}')
print(f'zeros count={zc}')

#2) if a)I/P= 1024 ,O/P= 7. b)I/P=256 , O/P= 13. sum out number of elemet in ithe given input.

n=int(input('enter no: '))
sum=0
while n>0:
    x=n%10
    sum=sum+x
    n//=10
print(f'sum={sum}')


# 3) if a)I/P= 123 ,O/P= 6. b)I/P=546 , O/P= 120.find  product of number of elements in the given input.
n=int(input('enter no: '))
prod=1
if n==0:
    prod=0
else:
    while n>0:
        x=n%10
        if x==0:
            n//=10
            continue
        else:
            prod=prod*x
        n//=10
print(f'product={prod}')

