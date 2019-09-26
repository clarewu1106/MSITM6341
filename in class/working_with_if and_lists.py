groceries = {"Apple", "Orange", "Steak", "Chicken"}

if "Penapple" not in groceries:
    print("we have apples")
else:
    print("we do not have apples")


age = 15

if age < 2:
    print("Baby")
else:
    if age < 4:
        print("Toddler")
    else:
        if age < 14:
            print("Kids")
        else:
            if age < 20:
                print("Teenagers")
            else:
                if age < 65:
                    print("Adults")
                else:
                    print("Elder")


if age< 2:
    print("Baby")
elif age< 4:
    print ("Toddler")
elif age< 14:
    print("kids")
elif age< 20:
    print("teenagers")    
elif age< 65:
    print("adults")
else:
    print("Elder")
   