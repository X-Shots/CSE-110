class account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"{self.name} - ${self.balance:.2f}"
     
    def getbalance(self):
        return self.balance

accounts = []
print("Enter the names and balances of bank accounts (type: quit when done)")
ans = ""
while ans.lower() != "quit":
    ans = input("What is the name of this account? ")
    if ans.lower() != "quit":
        ans2 = input("What is the balance? ")
        accounts.append(account(ans,ans2))
print()
print("Account Information:")
for x in accounts:
    print(x)




total = 0




for x in accounts:
    total += x.balance()
print(f"Total: {total}")
print(f"Average: {total/len(accounts):.2f}")
