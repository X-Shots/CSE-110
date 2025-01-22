grade = int(input("\nPLease enter your grade from 1 to 100 "))

if grade >= 90:
    grade = "A"
elif grade >= 80:
    grade = "B"
elif grade >= 70:
    grade = "C"
elif grade >= 60:
    grade = "D"
else:
    grade = "F"
    
print(f"\nYour grade is: {grade}")

