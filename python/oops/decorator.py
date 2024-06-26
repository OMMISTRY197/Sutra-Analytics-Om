#first method
def om(func):
    def world():
      print("Hello")
      func()
      print("Thank You")
    return world
@om
def hello():
    print("All Tasks...")
hello()

#_____________
print()
#_____________

#second method
def decorator(func):
    def wrapper():
        print("Transaction Initiated")
        func()
        print("Transaction Completed")
    return wrapper
# @decorator
def task():
    print("...Executing all steps of transaction...")
# task()
final = decorator(task)
final()