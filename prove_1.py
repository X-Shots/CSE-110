print("Enter colors you would like to see in an abstract phone wallpaper, type done to stop ")
colors = []
x = input("Please type a color ")
while(x!= "done"):
    colors.append(x)
    x = input("Please type a color ")

print("your walpaper should inclue the following colors:")
print()
for x in colors:
    print(x) 
    
print()    
print("Here is a prompt to give to an AI to make your wallpaper:")
print()
print("Please generate an abstact phone walpaper with these colors:",colors)
