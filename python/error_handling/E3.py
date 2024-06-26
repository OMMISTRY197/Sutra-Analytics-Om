# # working of try() 
# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional Part as Answer
#         result = x // y
#         print("Yeah ! Your answer is :", result)
#     except ZeroDivisionError:
#         print("Sorry ! You are not dividing by zero ")
 
# # Look at parameters and note the working of Program
# divide(10,5)
# divide(10,0)


def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except TypeError:
       # By this way we can know about the type of error occurring
        print("please enter a number,  type error")
    except ZeroDivisionError:
        print("Not divisible by 0, zero division error")

divide(10,"GFG") 
divide(10,0)
divide(10,3)