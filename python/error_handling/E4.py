 # define Python user-defined exceptions
# class om(Exception):
#     """Base class for other exceptions"""
#     pass
 
class arya(Exception):
    """Raised when the input value is zero"""
    pass
 
try:
    i_num = int(input("Enter a number: "))
    if i_num == 0:
        raise arya
except arya:
    print("Input value is zero, try again!")