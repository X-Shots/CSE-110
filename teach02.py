list = ["First name: ", "Last name: ", "Email address: ", "Phone number: ", "Job title: ", "ID Number: "]
print("Please enter the following information:")
print()
i = 0
for x in list:
    list[i] = input(list[i])
    i = i + 1
list[1] = list[1].upper()
list[4] = list[4].title()
list[2] = list[2].lower()


print()
print("The ID Card is:")
print("----------------------------------------")
print(f"{list[1]}, {list[0]}")
print(list[4])
print(f"ID: {list[5]}")
print()
print(list[2])
print(list[3])
print("----------------------------------------")
