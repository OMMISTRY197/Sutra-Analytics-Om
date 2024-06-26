def sum(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

def mul(*a):
    mul = 1
    for i in a:
        mul*=i
    return mul

def sub1(*args):   #from starting
    sub1 = args[0]
    for num in args[1:]:
        sub1 = sub1-num
    return sub1

def sub2(*args): #from ending
    l1 = args[::-1]
    sub2 = l1[0]
    for num in l1[1:]:
        sub2 = sub2-num
    return sub2
