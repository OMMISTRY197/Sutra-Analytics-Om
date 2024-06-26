class A:
    def __func(self,a,b,c):
        __sum1 = a+b+c
        return __sum1
    
class B(A):
    def mod(self,a,b):
        mod = a % b
        A.__sum1 = a+b
        return mod,A.__sum1
    
obj = B()
print(obj._A__func(1,2,3)) #accessing private method from derived class
print(obj.mod(10,20)) #accesing private variable from derived class
#unpacking variables
mod,sum1 = obj.mod(10,20)
print(mod)
print(sum1)

#ahi aapde private method ne tena derived class mathi use kari sakiye chhiye. 
# tena mate derived class ne call karvo pade. variable ane method em banne ma 
# kari sakiye. variable mate (classname.variablename) & method mate (_classname.methodname).