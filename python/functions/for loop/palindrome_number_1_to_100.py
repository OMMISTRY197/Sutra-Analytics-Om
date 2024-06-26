rev_num = 0
digit = 0

def palindrome():
    return palindrome

for i in range(10,101):
    num = i
    while num > 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num =  num // 10 
    if i == rev_num :
        print(i)
    rev_num = 0