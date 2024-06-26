def intro(**student):

    for key, value in student.items():
        print("{} is: {}".format(key,value))

intro(Firstname="om", Lastname="mistry", Age=17, Phone=9879853680)
intro(Firstname="mahir", Lastname="mistry", Email="mahir123@gmail.com", Country="India", Age=19, Phone_number=9876543210)