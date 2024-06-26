# Multilevel Inheritance

class A:
    def func(self,a,b,c):
        sum = a+b+c
        return sum

class B(A):
    def mul(self,a,b):
        mul = a * b
        return mul

class C(B):
    def sub(self,a,b):
        sub = a - b
        return sub
    
obj = C()

print(obj.func(10,20,30))