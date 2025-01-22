class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

shopingCart = []
ans = -1
while ans != 5:
    
    ans = int(input("\nPlease select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\nPlease enter an action: "))
    if ans == 1:
        item = input("\nWhat item would you like to add? ")
        price = float(input(f"\nWhat is the price of '{item}'? "))
        shopingCart.append(Item(item, price))
        print(f"\n{item} has been added to the cart")
    elif ans == 2:
        for i, item in enumerate(shopingCart):
            print(f"{i + 1}. {item}")
    elif ans == 3:
        remove = input("\nWhich item would you like to remove? ")
        found = False
        for x in shopingCart:
            if x.name.lower() == remove.lower():
                shopingCart.remove(x)
                print("\nItem removed.")
                found = True
            
            
        if not found:
            print("\nThat item is not in the shopping cart please try again")
    elif ans == 4:
        total = 0
        for x in shopingCart:
            total += x.price
        print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")
    





    
