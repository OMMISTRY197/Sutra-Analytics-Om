#  Hybrid Inheritance

class A:
    def func(self,a,b,c):
        sum = a+b+c
        return sum
    
class B():
    def mul(self,a,b):
        mul = a * b
        return mul

class C(A):
    def sub(self,a,b):
        sub = a - b
        return sub

class D(B):
    def div(self, a,b):
        div = a/b
        return div
    
class E(A,B):
    def mod(self, a,b):
        mod = a % b
        return mod


obj = E()
obj1 = C()
obj3 = D()
