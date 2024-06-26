# Display the famous place of any 5 cities as per the choice.

def cities(city):
    if city == "ahmedabad":
        return "famous place of ahmedabad is \'Kakaria\'"
    elif city == "surat":
        return "famous place of Surat is \'Dumas Beach\'"
    elif city == "bhavnagar":
        return "famous place of Bhavnagar is \'Bhavani Beach\'"
    elif city == "vadodara":
        return "famous place of Vadodara is \'MSU\'"
    elif city == "bharuch":
        return "famous place of bharuch is \'Golden Bridge\'"
    else:
        return "please enter the valid city"
    
city = ["ahmedabad","surat","bhavnagar","vadodara","bharuch"]
user = input("enter the city: ").lower()
print(cities(user))