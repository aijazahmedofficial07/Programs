#1)

row=int(input('enter no of rows: '))
for i in range(row+1):
    print('* '*i)



##OR##

'''row=int(input('enter no of rows: '))
for i in range(row,0,-1):
    print(''*(row-1)+'* '*i)

row=int(input('enter no of rows: '))
val=ord('A')
for i in range(row):
    #val=ord('A')
    for j in range(1+i):
        print(chr(val),end=' ')
        #val+=1
    print()
    #val+=1

row=int(input('enter no of rows: '))
val=1
for i in range(row):
    #val=1
    for j in range(1+i):
        print(val,end=' ')
        #val+=1
    print()
    #val+=1'''

#2)
'''row=int(input('enter row:'))
for i in range(row,0,-1):
    print('* '*i)'''

    #or#

row=int(input('enter row:'))
for i in range(row,0,-1):           #for i in range(row):
    for j in range(i):              #for j in range(i,row):
        print('*',end=' ')
    print()

#3)
row=int(input('enter row: '))
spc=2*(row-2)
for i in range(row):
    for j in range(spc):
        print(' ',end=' ')
    spc=spc-1
    for j in range(i+1):
        print('*',end=' ')
    print()

#4)

row=int(input('enter row: '))
for i in range(row,0,-1):
    print('  '*(row-i)+ '* '*i)