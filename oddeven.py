'''n=int(input("enter no : "))
if n%2==0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')

##OR##

n=int(input("enter no: "))
if ((n//2)*2)==0:
    print('even')
else:
    print('odd')

##OR##

n=int(input('enter no:'))
L1=['even','odd']
print(L1[n%2])'''

##OR##
n=int(input('enter no: '))
res='even' if n%2==0 else 'odd'
print(res)
