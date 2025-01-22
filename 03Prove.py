
num_drinks = 0

child_price = float(input("\nWhat is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults  = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate(%)? "))
print("Would you like to add some drinks for $1 per drink?")
who_thought_boolean_was_a_good_name = input('Type "Yes" if you would like to add drinks or "No" if you would not like drinks. ')

if(who_thought_boolean_was_a_good_name == "Yes" or who_thought_boolean_was_a_good_name == "yes"):
    num_drinks = int(input("How many drinks would you like?"))

sub = child_price * num_children + adult_price * num_adults + num_drinks
tax_amt = (sub) * tax / 100

print(f"\nSubtotal: ${sub:.2f}")
print(f"Sales tax: ${tax_amt:.2f}")
print(f"Total: ${(sub + tax_amt):.2f}")

pmt = float(input("\nWhat is the payment amount? "))
print(f"Change: ${(pmt - (sub + tax_amt)):.2f}")


