# def fact(n):
#     if n==1:
#         return n
#     else:
#         mul = n*fact(n-1)
#         return mul
    
# n = int(input("Ennter N:"))
# print(fact(n))

def sum1(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum1(lst[1:])
lst = [5,10,15,20,25]
print(sum1(lst))