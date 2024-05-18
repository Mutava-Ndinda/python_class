def add(x,y):
    result = x+y
    return result

def sub(m,n):
    result = m-n
    return result

def div(m,n):
    result = m/n
    return result

def prod(a,b):
    result = a*b
    return result

def mod(j,f):
    result = j%f
    return result

def sum(*numbers):
    total = 0
    for nums in numbers:
        total+=nums
    return total

def multipymany(*ints):
    product=1
    for int in ints:
        product*=int
    return product