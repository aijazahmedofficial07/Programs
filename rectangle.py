row=int(input('enter no of rows: '))
col=int(input('enter no of cols: '))
for i in range(row):
    for j in range(col):
        print('*',end=' ')
    print()

row=int(input('enter no of rows: '))
col=int(input('enter no of cols: '))    
for i in range(1,row+1):
    for j in range(col):
        print(i,end=' ')
    print()

row=int(input('enter no of rows: '))
col=int(input('enter no of cols: ')) 
for i in range(row):
    for j in range(col,0,-1):
      print(j,end=' ')
    print()

row=int(input('enter no of rows: '))
col=int(input('enter no of cols: '))
val=ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=' ')
        val+=1
    print()

row=int(input('enter no of rows: '))
col=int(input('enter no of cols: '))
val=ord('A')
for i in range(row):
    val=ord('A')
    for j in range(col):
        print(chr(val),end=' ')
        val+=1
    print()

row=int(input('enter no of rows: '))
col=int(input('enter no of cols: '))
val=ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val),end=' ')
    print()
    val+=1

row=int(input('enter no of rows: '))
col=int(input('enter no of cols: '))
val=ord('A')+row-1
for i in range(val,ord('A')-1,-1):
    for j in range(col):
        print(chr(i),end=' ')
    print()