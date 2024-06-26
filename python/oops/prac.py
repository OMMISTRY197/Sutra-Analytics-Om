#class & object

# class dataAnalytics:
#     def math(a,b):
#         return a+b
    
# a = dataAnalytics
# # a.math()
# print(a.math(12,13))

# Simple Inheritance

class base:
    def sum(self,a,b,c):
        sum1 = a+b+c
        return sum1
    def sub(self,a,b):
        sub1 = a-b
        return sub1
    
obj = base()

a = obj.sum(11,12,13)
b = obj.sum(10,20,30)

print(a)
print(b)