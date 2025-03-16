def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited"))
    if amount < 0:
        print("Thats not a valid entry")

def withdraw():
    pass
balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("thats not a valid choice")