accounts={101:50000,102:45000,103:55000}
print("Current Account Present:")
print(accounts)
id=int(input("Enter Account Id:"))
amt= int(input("enter amount:"))
balance=accounts.get(id)
print(balance)
if balance==None:
    accounts [id]=amt
    print("New Account Created")
else:
    newbalance=balance+amt
    accounts[id]=newbalance
    print("Account updated")
print("Account Details:")
print(accounts)