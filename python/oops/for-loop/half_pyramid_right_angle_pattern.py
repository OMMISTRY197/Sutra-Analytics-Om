class pattern:

    def pyramid(self):
        self.rows = int(input("Enter number: "))
        for row in range(1,self.rows+1):
            for column in range(row):
                print("*",end=" ")
            print()

obj = pattern()
obj.pyramid()

