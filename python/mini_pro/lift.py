def find_nearest_lift(person_floor, lift1_floor, lift2_floor):
    distance_lift1 = (person_floor - lift1_floor) 
    distance_lift2 = (person_floor - lift2_floor) 
    
    if distance_lift1 < 0:
        distance_lift1 = -distance_lift1
    if distance_lift2 < 0:
        distance_lift2 = -distance_lift2

    if person_floor == lift1_floor:
        return "Use Lift 1"
    elif person_floor == lift2_floor:
        return "Use Lift 2"
    elif distance_lift1 == distance_lift2:
        return "Use Lift 1"
    elif distance_lift1 < distance_lift2:
        return "Use Lift 1"
    elif distance_lift1 > distance_lift2:
        return "Use Lift 2"
    else:   #lift at same floor
        return "Use lift 1"

person_floor = int(input("Enter the current floor of the person: "))
if person_floor > 10:
    print("Your building has only 10 floors.")
else:
    lift1_floor = int(input("Enter the floor where is the lift 1: "))
    lift2_floor = int(input("Enter the floor where is the lift 2: "))
    if lift1_floor > 10 or lift2_floor > 10:
        print("Your building has only 10 floors.")
    else:
        print(find_nearest_lift(person_floor, lift1_floor, lift2_floor))