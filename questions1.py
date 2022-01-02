# 1) series=2,1,4,2,6,3,8,4,10,5.......   , if user gives input as input=3 then output=2,1,4.

n= int(input('enter no: '))
even=2
nat=1
for i in range(1,n+1):
    if i%2==0:
        print(nat,end=' ')
        nat+=1
    else:
        print(even,end=' ')
        even+=2


#  2) print a sreies of square of numbers

n=int(input('enter no of element contain in series: '))
print(f'series of squares till {n} is: ')
for i in range(1,n+1):
    print(i*i,end=' ')

# 3) sreies=0 1 1 2 3 5 8 if input= 4 , output= 0 1 1 2
# explaination x=0,y=1 => y1=0+1=1   .  y=x1=1,y1=1 => y2=1+1=2 . hence result is 0 1 1 2

n=int(input('enter no of element contain in series: '))
x=0
y=1
for i in range(n):
    print(x,end=' ')
    z=x+y
    x=y
    y=z

# 4) if a)I/P= 1024 ,O/P=4. b)I/P=256 , O/P=3. count number of elemet in ithe given input.

n=int(input('enter no: '))
c=0
while n>0:
    c+=1
    n//=10
print(c)

#OR#

n=int(input('enter no: '))
print(len(str(n)))


# 5) if a)I/P= 123 ,O/P=321. b)I/P=256 , O/P=652. reverse number of elemet in ithe given input.

n=int(input('enter no: '))
r=0
while n>0:
    x=n%10
    r=r*10+x
    n//=10
print(r)