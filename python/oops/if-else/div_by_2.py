class division():
    def div(self,num):
        if num %2 == 0:
            return "number is div by 2"
        else:
            return "number is not divisible by 2"
        
obj = division()
a = obj.div(int(input('Enter Number: ')))
print(a)