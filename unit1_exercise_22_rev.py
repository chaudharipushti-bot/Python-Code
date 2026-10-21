# 2.10 ATM PIN Simulator (With Balance Management)

CORRECT_PIN_value = "1234"
attempts_value = 3
balance_value = 5000.0  # Setting a starting balance for the user
authenticated_value = False

# Part 1: PIN Verification Loop
while attempts_value > 0:
    entered_pin_value = input("Enter your 4-digit PIN: ")
    
    if entered_pin_value == CORRECT_PIN_value:
        print("Access Granted!\n")
        authenticated_value = True
        break
    else:
        attempts_value -= 1
        print(f"Incorrect PIN. Attempts remaining: {attempts_value}")

if attempts_value == 0:
    print("Card Blocked! Too many incorrect attempts.")

# Part 2: ATM Transaction Menu (Runs only if PIN is correct)
while authenticated_value:
    print("----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit (Save) Money")
    print("4. Exit")
    
    choice_value = input("Select an option (1-4): ")
    
    if choice_value == "1":
        print(f"Your current balance is: Rs. {balance_value}\n")
        
    elif choice_value == "2":
        withdraw_amount_value = float(input("Enter amount to withdraw: "))
        if withdraw_amount_value > balance_value:
            print("Transaction Failed: Insufficient funds!\n")
        elif withdraw_amount_value <= 0:
            print("Transaction Failed: Invalid amount!\n")
        else:
            balance_value -= withdraw_amount_value
            print(f"Rs. {withdraw_amount_value} withdrawn successfully.")
            print(f"Remaining Balance: Rs. {balance_value}\n")
            
    elif choice_value == "3":
        deposit_amount_value = float(input("Enter amount to deposit: "))
        if deposit_amount_value <= 0:
            print("Transaction Failed: Invalid amount!\n")
        else:
            balance_value += deposit_amount_value
            print(f"Rs. {deposit_amount_value} deposited successfully.")
            print(f"New Balance: Rs. {balance_value}\n")
            
    elif choice_value == "4":
        print("Thank you for using the ATM. Goodbye!")
        break  # Exits the ATM menu loop
        
    else:
        print("Invalid choice! Please select a valid option.\n")
