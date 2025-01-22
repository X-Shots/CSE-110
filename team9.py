#print("Enter a list of numbers type zero when finsihed.")
ans = -1
numbers = []
while ans != 0:
    ans = int(input("Enter a list of numbers type zero when finsihed."))
    if ans != 0:
        numbers.append(ans)

print(f"The sum is: {sum(numbers)}")

print(f"The average is: {sum(numbers)/len(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The smallest number is: {min(numbers)}")
print(numbers.sort())