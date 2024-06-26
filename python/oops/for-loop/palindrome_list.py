class Palindrome:
    list1 = [111, 112, 555, 108, 101, 545, 112]
    palindrome_list = []

    def check_palindromes(self):
        result_list = []  
        for i in self.list1:
            num = i
            rev_num = 0
            while num > 0:
                digit = num % 10
                rev_num = rev_num * 10 + digit
                num = num // 10
            if i == rev_num:
                self.palindrome_list.append(i)
                result_list.append([i, True])  
            else:
                result_list.append([i, False])  

        print("Output:", result_list) 

p = Palindrome()
p.check_palindromes()