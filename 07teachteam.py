import random 

num = random.randint(1,100)

count = 0

guess = ""
ans = "yes"
while ans.lower() == "yes":
    guess = ""
    num = random.randint(1,100)
    while guess != num:
        
        guess = int(input("\nWhat is your guess? "))
        if guess > num:
            print("Lower")
        elif guess < num:
            print("Higher")
        else:
            print("You guessed it!")
        count += 1
    print(f"You took {count} guesses to get it right!")
    ans = input("Would you like to play again?(Yes/No)")

    
