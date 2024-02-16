"""Write a Python program to replicate a Banking system. The following features are mandatory:
1.Account login
2. Amount Depositing
3. Amount Withdrawal
Other than the above features you can add any other also."""
class BankOperations:
    def __init__(self,account_number,pin,balance=0):
        self.account_number=account_number
        self.pin=pin
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit of {amount} rupees was successful.")
        else:
            print("Invalid deposit amount.")
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f'Withdrawal of {amount} rupees was successful.')
        else:
            print("Insufficient fund or invalid withdrawal amount")
    def check_balance(self):
        print(f"Current balance: {self.balance}")
def main():
    user_accounts={"47589":{"pin":"1234","balance":1350},
                   "12456":{"pin":"9658","balance":2478},
                   "45632":{"pin":"6523","balance":4500},
                   "85236":{"pin":"1874","balance":500},
                   "74256":{"pin":"5284","balance":1000}}
    #login
    while True:
        print("\nMenu")
        print("1. Login")
        print("2. Exit")
        choice=input("enter your choice: ")

        if choice=="1":
            account_number=input("Enter your account number:")
            if account_number in user_accounts:
                pin=input("Enter pin:")
                if pin==user_accounts[account_number]["pin"]:
                    account=BankOperations(account_number, pin,user_accounts[account_number]["balance"])
                    account_menu(account)
                    break
                else:
                    print("Invalid pin. Please try again")
            else:
                print("Account not found, Please try again")
        elif choice=="2":
            print("Exiting program. Good bye!")
            break
        else:
            print("Invalid choice. Please enter a valid option")

def account_menu(account):
    while True:
        print("\n Account menu ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice=="1":
            amount=float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice=="2":
            amount=float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice=="3":
            account.check_balance()
        elif choice=="4":
            print("Logging out. Good bye!")
            break
        else:
            print("invalid choice.Please enter a valid choice")
if __name__=="__main__":
    main()








