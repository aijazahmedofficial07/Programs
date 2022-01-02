#1)
row=int(input('enter rows: '))
spc=row-1
str=1
for i in range(row):
    for j in range(spc):
        print(' ',end=' ')
    for k in range(str):
        print('*',end=' ')
    print()
    str+=2
    spc-=1

#2)
row=int(input('enter rows: '))
spc=0
str=2*row-1
for i in range(row):
    for j in range(spc):
        print(' ',end=' ')
    for k in range(str):
        print('*',end=' ')
    print()
    str-=2
    spc+=1

#3)
row=int(input('enter rows: '))
for i in range(row+1):
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(row-1):
    for k in range(row-1-i):
        print('*',end=' ')
    print()

#4)
row=int(input('enter rows: '))
for i in range(row):
    for j in range(row-i):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()
for i in range(row):
    for j in range(i):
        print(' ',end=' ')
    for k in range(row-i):
        print('*',end=' ')
    print()

#5)
row=int(input('enter rows: '))
for i in range(row):
    for j in range(row-i):
        print(' ',end='')
    for k in range(i):
        print('*',end=' ')
    print()
for i in range(row):
    for j in range(i):
        print(' ',end='')
    for k in range(row-i):
        print('*',end=' ')
    print()