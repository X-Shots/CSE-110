
# base rules
age1 = int(input("\nWhat is the age of the first rider? "))
height1 = int(input("What is the height of the first rider in inches? "))
if age1 > 11 and age1 < 18:
    passport = input("Do you have a Golden Passport(yes/no)?")
    if passport.lower() == "yes":
        age1 = 18


age2 = -1
height2 = -1

two = input("\nIs there a second rider (yes/no)?")
if two.lower() == "yes":
    age2 = int(input("\nWhat is the age of the second rider? "))
    height2 = int(input("What is the height of the second rider in inches? "))
    if age2 > 11 and age2 < 18:
        passport = input("Do you have a Golden Passport(yes/no)?")
        if passport.lower() == "yes":
            age1 = 18

if (age1 < 18 and age2 < 18) and age1 >= age2:
    older = age1
    younger = age2
else:
    older = age2
    younger = age1

if height2 > 0:   
    if height1 < 36 or height2 < 36:
        print("\nSorry, you may not ride.")
elif age2 < 0 and age1 >= 18 and height1 > 61:
    print("\nWelcome to the ride. Please be safe and have fun!")
elif age1 >=18 or age2 >= 18:
    print("\nWelcome to the ride. Please be safe and have fun!")
    
elif (age1 > 11 and age2 > 11) and (height1 > 51 and height2 > 51):
    print("\nWelcome to the ride. Please be safe and have fun!")

elif older > 15 and younger > 13:
    print("\nWelcome to the ride. Please be safe and have fun!")
    
else:
    print("\nSorry, you may not ride.end")
    
    




