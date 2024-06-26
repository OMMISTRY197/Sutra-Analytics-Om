# hierarchical Inheritance

class A:
    def func(self,a,b,c):
        sum = a+b+c
        return sum
    
class B(A):
    def mul(self,a,b):
        mul = a * b
        return mul

class C(A):
    def sub(self,a,b):
        sub = a - b
        return sub

class D(A):
    def div(self, a,b):
        div = a/b
        return div
    
class E(A):
    def mod(self, a,b):
        mod = a % b
        return mod