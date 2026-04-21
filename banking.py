class BankingSystem:
    def __init__(self,name,balance,loan):
        self.name = name
        self.balance = balance
        self.loan = loan
accounts = []

def add_account():
    name =  input("Enter name :- ")
    balance = int(input("Enter initial balance:- "))
    loan = int(input("Enter loan ammount :- "))
    accounts.append(BankingSystem(name,balance,loan))
    print("Account added succesfully!")


def withdraw():
    name = input("Enter name :- ")
    for acc in accounts:
        if acc.name == name:
            ammount = int(input("Enter ammount to withdraw:- "))
            acc.balance -= ammount
            print(f"Your Withdrawal of {ammount} is succesfull, Now your balance is {acc.balance}")
        else:
            print("No account found")

def deposite():
    name = input("Enter name :- ")
    for acc in accounts:
        if acc.name.lower() == name.lower():
            ammount = int(input("Enter ammount to withdraw:- "))
            acc.balance += ammount
            print(f"Your deposite of {ammount} is succesfull, Now your balance is {acc.balance}")
        else:
            print("No account found")

def check_balance():
    name = input("Enter your name :- ")
    for acc in accounts:
        if acc.name.lower() == name.lower():
            print(f"Mr/Ms {acc.name} your account balance is {acc.balance}")
        else:
            print("Account not found")


def add_loan():
    name = input("Enter name:- ")
    for acc in accounts:
        if acc.name.lower() == name.lower():
            ammount = int(input("Enter Loan ammount:- "))
            acc.loan += ammount
            print("Loan is successfull")
        else:
            print("Account not found")


def cal_interest():
    name = input("Enter name:- ")
    for acc in accounts:
        if acc.name.lower() == name.lower():
            time = int(input("Enter time in years:- "))
            rate = int(input("Enter rate of interest:- "))
            interest = acc.loan * time * rate / 100
            print(f"Mr/Ms {acc.name} your loan of {acc.loan} is successfull , your Simple interest is {interest}")

        else:
            print("Account not found")


def pay_loan():
    name = input("Enter Your name:- ")
    for acc in accounts:
        if acc.name.lower() == name.lower():
            ammount = int(input("Enter ammount:- "))
            acc.loan -= ammount
            print(f"The loan of {ammount} is paid, your loan balance is {acc.loan}")
        else:
            print("Account not found")


def transfer():
    sender_name = input("Enter sender name:- ")
    receiver_name = input("Enter receiver name:- ")
    for acc in accounts:
        if acc.name.lower() == sender_name.lower():
            ammount = int(input("Enter ammount to transfer:- "))
            acc.balance -= ammount
            for acc in accounts:
                if acc.name.lower() == receiver_name.lower():
                    acc.balance += ammount
                    print(f"Transfer of {ammount} from {sender_name} to {receiver_name} is successful.")
                    break
                else:
                    print("Receiver account not found.")

def delete_account():
    name = input("Enter name:- ")
    for acc in accounts:
        if acc.name.lower() == name.lower():
            accounts.remove(acc)
            print("Account deleted successfully")
            return
    print("Account not found")
    
def show_all_accounts():
    if not accounts:
        print("No accounts available")
    else:
        for acc in accounts:
            print(f"Name: {acc.name}, Balance: {acc.balance}, Loan: {acc.loan}")
            
while True:
    print("1. Add Account")
    print("2. Withdraw")
    print("3. Deposite")
    print("4. Check Balance")
    print("5. Add Loan")
    print("6. Calculate Interest")
    print("7. Pay Loan")
    print("8. Transfer")
    print("9. Delete Account")
    print("10. Show All Accounts")
    print("11. Exit")

    choice = int(input("Enter your choice:- "))

    if choice == 1:
        add_account()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        deposite()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        add_loan()
    elif choice == 6:
        cal_interest()
    elif choice == 7:
        pay_loan()
    elif choice == 8:
        transfer()
    elif choice == 9:
        delete_account()
    elif choice == 10:
        show_all_accounts()
    elif choice == 11:
        break
    else:
        print("Invalid choice, please try again.")
