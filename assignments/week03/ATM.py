balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            print("Balance:", balance)
            
        elif choice == "2":
            amount = int(input("Withdraw amount: "))
            if amount <= balance:
                balance -= amount
                print("New balance:", balance)
            else:
                print("Not enough money!")
                
        elif choice == "3":
            amount = int(input("Deposit amount: "))
            balance += amount
            print("New balance:", balance)
            
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice")