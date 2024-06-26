class A:
    def __func(self,a,b,c):  #private method
        sum = a+b+c
        return sum

class B():
    def mul(self,a,b): #public method
        mul = a * b
        return mul

class C(B):
    def _sub(self,a,b):  #protected method
        sub = a - b
        return sub
    
obj = C()
obj1 = A()
print(obj1._A__func(10,20,30))  #calling object of private class method
print(obj._sub(10,20)) #calling object of protected class method
print(obj.mul(10,20)) #calling object of public class method from protected class
