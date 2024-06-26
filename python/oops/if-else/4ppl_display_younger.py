class age:
	def young(self,age1,age2,age3,age4):
            if age1<age2 and age1<age3 and age1<age4:
                print("The Youngest Age is om")
            elif age2<age1 and age2<age3 and age2<age4:
                print("The Youngest Age is aryan")
            elif age3<age1 and age3<age2 and age3<age4:
                print("The Youngest Age is rudraksh")
            elif age1==age2:
                 print("om and aryan are young")
            elif age1==age3:
                 print("om and rudraksh are young")
            elif age1==age4:
                 print("om and mahir are young")
            elif age2==age3:
                 print("aryan and rudraksh are young")
            elif age2==age4:
                 print("aryan and mahir are young")
            elif age3==age4:
                 print("rudraksh and mahir are young")
            else:
                print("The Youngest Age is mahir")
        
age1 = int(input("Enter the Age of om:"))
age2 = int(input("Enter the Age of aryan:"))
age3 = int(input("Enter the Age of rudraksh:"))
age4 = int(input("Enter the Age of mahir:"))

obj = age()
obj.young(age1,age2,age3,age4)