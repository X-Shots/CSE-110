import random
num = int(random.random() * 10 + 1)
print(num)
guess = 0
while int(guess) != num:
    guess = int(input("\nPlease enter your guess of the number from one to 10"))
    if guess > num:
        print("\nThe number is lower!")
    elif guess < num:
        print("\nThe number is higher!")
    elif guess == num:
        print("\nCorrect!")
    else:
        print("I'm a bad programmer")
