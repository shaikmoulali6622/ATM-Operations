# Initial balance
balance = 1000.0

# ATM Menu
def show_menu():
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# ATM Operation Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is ₹{balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter the amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: ₹"))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
