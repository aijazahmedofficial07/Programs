def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
a,b=swap(10,20)
print(f'a={a} and b={b}')
