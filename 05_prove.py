player1_cash = 0
player2_cash = 0

num = 0

while num < 1:
    ans = input("\nYour friend asks you if you would rather be stuck below a FOREST or thrown to the bottom of the Pacific OCEAN. ")

    if ans.lower() == "forest":
    
        num = 1
    
    elif ans.lower() == "ocean":
        
        num = 2

if num == 1:
    ans = input("\nBefore teleporting you into a forest, your friend gave you a potion.\nYou can either DRINK the potion or SMASH it into a wall. ")
    if ans.lower() == "drink":
        print("\nThe potion turns you into a huge albino naked mole rat.\nYou can now freely burrow underneath the forest. ")
        ans = input("\nYou can either burrow BELOW, to the LEFT, or contiune FORWARD.\nWhich way would you like to go? ")
        if ans.lower() == "below":
            print("\nWhoops too far! you fall into a pit of lava burn to a crisp")
            
            player1_alive = False
            player1_cash = 0
        elif ans.lower() == "left":
            print("\nYou find yourslef in the home of another naked mole rat. They give you $19.87 and you live with them for the rest of your life.")
            player1_alive = True
            player1_cash = 19.87
        elif ans.lower() == "forward":
            print("\nYou find the underground rat metroplex. You find a job as an Investment Banker and make $100,000,000!")
            player1_alive = True
            player1_cash = 100000000
        else:
            print("\nWrong answer lol")
            player1_alive = False
            player1_cash = 0
    elif ans.lower() == "smash":
        ans = input("\nThe potion undergoes an intese chemical reaction with the forest air.\nIt starts expanding and heats up to 9983493483498 degrees kelvin.\n You can either CRY or PRAY for help. ")
        if ans.lower() == "cry":
            print("\nThe potion burns you to a crisp.")
            player1_alive = False
        elif ans.lower() == "pray":
            print("\nAn angle comes to your rescure and teleports you back home. You post your story on Reddit and make $2000 from veiws.")
            player1_alive = True
            player1_cash = 2000
        else:
            print("\nwrong answer you lose!")
            player1_alive = False
            player1_cash = 0
    else:
        print("\nMisclick I hope")
        player1_alive = False
        player1_cash = 0

            
            

        
    

else:
    ans = input("\nYour friend tells you you can pick either an OCRA or a DOLPHIN. ")
    if ans.lower() == "ocra":
        ans = input("\nYou are on the ocean with your rented speed boat. You see a heard of Ocras in the water. You can either use the JETSKI to escape or finish your FORTNITE game. It is a new season after all. ")
        if ans.lower() == "jetski":
            print("\nYou sucsessfuly make it to the shore where Elon Musk thanks you for returning his beloved Ocras. He gives you all of his Tesla shares which are worth approximately $152299836378. ")
            player1_alive = True
            player1_cash = 152299836378
        elif ans.lower() == "fortnite":
            print("\nThe ocras headbutt your boat eventually flipping it over. You die after swimming for two days and are $20000 in debt from the speedboat.")
            player1_alive = False
            player1_cash = -20000
        else:
            print("\nThat's not an answer choice punk")
            player1_alive = False
            player1_cash = 0
    elif ans.lower() == "dolphin":
        ans = input("\nYou are stranded on a private island with a harpoon gun. You see some dolphins coming up to you. \nYou can either SHOOT the dolphins or SING for them to show your friendship. ")
        if ans.lower() == "shoot":
            print("\nJokes on you the dolphins are government spys and they lock you in a high security prison for the rest of your life.")
            player1_alive = True
            player1_cash = 0
        elif ans.lower() == "sing":
            print("\nThe dolphins love your song and bring you a cellphone to call for help, 4000 tacobell tacos, and $200000")
            player1_alive = True 
            player1_cash = 2000000
        else:
            print("\nCouldnt type it in eh?")
            player1_alive = False
            player1_cash = 0
    else:
        print("/nTake some typing classes")
        player1_cash = 0
        player1_alive = False
        
        
print("\n")
print("\nPass the laptop to the seccond player.")
        
    
        
num = 0

while num < 1:
    ans = input("\nYour friend asks you if you would rather be stuck below a FOREST or thrown to the bottom of the Pacific OCEAN. \nType 'OCEAN' or 'FOREST' to contiune...   ")

    if ans.lower() == "forest":
    
        num = 1
    
    elif ans.lower() == "ocean":
        
        num = 2

if num == 1:
    ans = input("\nBefore teleporting you into a forest, your friend gave you a potion.\nYou can either DRINK the potion or SMASH it into a wall. ")
    if ans.lower() == "drink":
        print("\nThe potion turns you into a huge albino naked mole rat.\nYou can now freely burrow underneath the forest. ")
        ans = input("\nYou can either burrow BELOW, to the LEFT, or contiune FORWARD.\nWhich way would you like to go?")
        if ans.lower() == "below":
            print("\nWhoops too far! you fall into a pit of lava burn to a crisp")
            
            player2_alive = False
            player2_cash = 0
        elif ans.lower() == "left":
            print("\nYou find yourslef in the home of another naked mole rat. They give you $19.87 and you live with them for the rest of your life.")
            player2_alive = True
            player2_cash = 19.87
        elif ans.lower() == "forward":
            print("\nYou find the underground rat metroplex. You find a job as an Investment Banker and make $100,000,000!")
            player2_alive = True
            player2_cash = 100000000
        else:
            print("\nWrong answer lol")
            player2_alive = False
            player2_cash = 0
    elif ans.lower() == "smash":
        ans = input("\nThe potion undergoes an intese chemical reaction with the forest air.\nIt starts expanding and heats up to 9983493483498 degrees kelvin.\n You can either CRY or PRAY for help. ")
        if ans.lower() == "cry":
            print("\nThe potion burns you to a crisp.")
            player2_alive = False
        elif ans.lower() == "pray":
            print("\nAn angle comes to your rescure and teleports you back home. You post your story on Reddit and make $2000 from veiws. ")
            player2_alive = True
            player2_cash = 2000
        else:
            print("\nwrong answer you lose!")
            player2_alive = False
            player2_cash = 0
    else:
        print("\nMisclick I hope")
        player2_alive = False
        player2_cash = 0

            
            

        
    

else:
    ans = input("\nYour friend tells you you can either have an OCRA or a DOLPHIN. ")
    if ans.lower() == "ocra":
        ans = input("\nYou are on the ocean with your rented speed boat. You see a heard of Ocras in the water. You can either use the JETSKI to escape or finish your FORTNITE game. It is a new season after all. ")
        if ans.lower() == "jetski":
            print("\nYou sucsessfuly make it to the shore where Elon Musk thanks you for returning his beloved Ocras. He gives you all of his Tesla shares which are worth approximately $152299836378. ")
            player2_alive = True
            player2_cash = 152299836378
        elif ans.lower() == "fortnite":
            print("\nThe ocras headbutt your boat eventually flipping it over. You die after swimming for two days and are $20000 in debt from the speedboat. ")
            player2_alive = False
            player2_cash = -20000
        else:
            print("\nThat's not an answer choice punk")
            player2_alive = False
            player2_cash = 0
    elif ans.lower() == "dolphin":
        ans = input("\nYou are stranded on a private island with a harpoon gun. You see some dolphins coming up to you. \nYou can either SHOOT the dolphins or SING for them to show your friendship. ")
        if ans.lower() == "shoot":
            print("\nJokes on you the dolphins are government spys and they lock you in a high security prison for the rest of your life.")
            player2_alive = True
            player2_cash = 0
        elif ans.lower() == "sing":
            print("\nThe dolphins love your song and bring you a cellphone to call for help, 4000 tacobell tacos, and $200000")
            player2_alive = True 
            player2_cash = 2000000
        else:
            print("\nCouldnt type it in eh?")
            player2_alive = False
            player2_cash = 0
    else:
        print("/nTake some typing classes")
        player2_cash = 0
        player2_alive = False

    
print("\n")
print("\nFinal standings:")
print(f"Player one alive: {player1_alive}")
print(f"Player two alive: {player2_alive}")
print(f"Player one's money: {player1_cash}")
print(f"Player two's money: {player2_cash}")
    
if player2_cash > player1_cash:
    print("\nPlayer two wins!")
elif player1_cash > player2_cash:
    print("\nPlayer one wins!")
elif player1_cash == player2_cash:
    print("Looks like there is tie! I guess you have to play again!")

print("\nThanks for playing!")

    