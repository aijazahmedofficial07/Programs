#write a program to fetch the first non repeating elemet from the list
def firstnonrepeatingelement(arr,n):
    for i in range(n):
        j=0
        while(j<n):
            if (i!=j and arr[i]==arr[j]):
                break
            j+=1
        if(j==n):
            return arr[i]
    return -1
arr=[]
x=int(input('enter no of element to enter:'))
for i in range(x):
    y=int(input('enter the no: '))
    arr.append(y)
n=len(arr)
print(arr)
print(firstnonrepeatingelement(arr,n))


#or#


arr=[]
x=int(input('enter no of element to enter:'))
for i in range(x):
    y=int(input('enter the no: '))
    arr.append(y)
n=len(arr)
print(arr)
for i in range(n):
    j=0
    while(j<n):
        if (i!=j and arr[i]==arr[j]):
            break
        j+=1
    if(j==n):
        print(arr[i])
        #break

