# 1)normally
l=[]
n=int(input('enter the no of elements: '))
for i in range(n):
    item=int(input(f'enter the {i}th item: '))
    l.append(item)
print(l)
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)

#or#


# 2)alternate
def bubblesort(list):
    n=len(list)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
list=[]
n= int(input('enter no of elements:'))
for i in range(n):
    item=int(input(f'enter the {i}th item: '))
    list.append(item)
print(list)
bubblesort(list)
print('sorted list is : ')
for i in range(len(list)):
    #print(list[i])
    print('% d' % list[i])