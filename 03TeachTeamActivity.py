import math
def compute_area_square(num):
    return compute_area_rectangle(num,num)
def compute_area_rectangle(x,y):
    return x * y
def compute_area_circle(num):
    return math.pi * math.pow(num,2)

def compute_area(shape, x, y):
    if shape.lower() == "rectangle":
        return compute_area_rectangle(x,y)
    if shape == "square":
        return compute_area_square(x)
    elif shape.lower() == "circle":
        return compute_area_circle(x)
    else:
        print("invalid input")
ans = ""

while ans.lower().strip() != "quit":
    ans = input("What kind of shape would you like to use?\nThe options are sqaure, rectangle, cirlce, or type 'quit' to quit ")
    if ans.lower().strip() != "quit" and ans.lower().strip() != "advanced":
        if ans.lower().strip() == "sqaure":
            num = float(input("\n what is the length of the side of the square? "))
            print(f"The area of your square is: {compute_area_square(num)}")
        elif ans.lower().strip() == "rectangle":
            x = float(input("\n what is the length of the first side of the rectangle? "))
            y = float(input("\n what is the length of the seccond side of the rectangle? "))
            print(f"The area of the rectangle is: {compute_area_rectangle(x,y)}")
        elif ans.strip().lower() == "circle":
            rad = float(input("What is the radius of your circle? "))
            print(f"The area of your cirlce is: {compute_area_circle(rad)}")
        else:
            print("invalid input please try again!")
    print()
    if ans.lower().strip() == "advanced":
        string = input("Enter the name of your shape(sqaure, rectangle, circle) followed by the correct number of sides seperated with commas.")
        parts = string.split(",")
        if len(parts) == 2:
            print(f"The area of your {parts[0]} is {compute_area(parts[0].lower().strip(),float(parts[1]), 0)}")
        elif len(parts) == 3:
            print(f"The area of your {parts[0]} is {compute_area(parts[0].lower().strip(),float(parts[1]), float(parts[2]))}")
        else:
            print("invalid input please try again")











        