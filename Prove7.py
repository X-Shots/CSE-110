print("Welcome to the guessing game")
word = "java"
guess = ""
trys = 0
hint = ""
for i in word:
    hint += "_ "
print(f"Your hint is: {hint}")

while(guess != word):
    
    guess = input("What is your guess? ")
    hint = ""
    num = 0
    if len(word) != len(guess):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        while(num < len(word)):
        
            if(word[num] == guess[num].lower()):
                hint += guess[num].upper()
                hint += " "
            elif word.find(guess[num]) != -1 :
                hint += guess[num].lower()
                hint += " "
            else :
                hint += "_ "
            num += 1
    if guess != word:
        print(f"Your hint is: {hint}")
    trys += 1
print("Congratulations! You guessed it!")   


if trys == 1 :
    print("Wow first try you must be a cheater")

else:
      print(f"It took you {trys} guesses.")
        
