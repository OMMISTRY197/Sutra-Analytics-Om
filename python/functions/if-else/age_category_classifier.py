# Age Category Classifier

def classifier(age):
    if age>=60:
        return "you are an adult"
    elif age>=30 and age<60:
        return "you are a young adult"
    elif age>=18 and age<30:
        return "you are a young"
    else:
        return "you are minor"
    
user = int(input("enter your age: "))
print(classifier(user))