class pattern:
        def get_rows(self):
            while True:
                user_input = input("Enter the number: ")
                self.number = int(user_input)
                break
        

        def pyramid(self):            
            for row in range(self.number):
                for space in range(self.number-row-1):
                    print(" ",end=" ")
                for column in range(row+1):
                    print("*",end=" ")
                print()

            for row in range(self.number-2,-1,-1):
                for space in range(self.number-row-1):
                    print(" ",end=" ")
                for column in range(row+1):
                    print("*",end=" ")
                print()
obj = pattern()
obj.get_rows()
obj.pyramid()