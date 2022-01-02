#write a program to verify that the entered number is prime number or not.

n=int(input('enter no: '))
c=0
lc=0
for i in range(2,(n//2)+1):
    lc+=1
    if n%i==0:
        c+=1
        break
if c==0:
    print(f'{n} is prime number')
else:
    print(f'{n} is not a prime number')
print(f'loop counter={lc}')