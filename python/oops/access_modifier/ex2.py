class A:
    def func(self,a,b,c): #public method
        sum = a+b+c
        return sum
    
class B():
    def _mul(self,a,b): #protected method
        mul = a * b
        return mul

class C(A):
    def __sub(self,a,b): #private method
        sub = a - b
        return sub

class D(B):
    def div(self, a,b): #public class & accesing protected method
        div = a/b
        return div
    
class E(A,B): #public class & accesing the public and ptotected method class
    def mod(self, a,b): 
        mod = a % b
        return mod


obj = E()
print(obj.func(10,25,50))
print(obj._mul(2,5))
obj1 = C()
print(obj1._C__sub(20,10))
print(obj1.func(20,10,30))
obj3 = D()
print(obj3._mul(10,5))
