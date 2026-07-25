EXCHANGE_RATE = 35.5
print("Currency Converter (THB <-> USD)")
print("1. THB to USD")
print("2. USD to THB")

choice = input("Choose conversion direction (1 or 2): ")
amount = float(input("Enter amount to convert: "))

if choice == "1":
    result = amount / EXCHANGE_RATE
    print(f"\nFormula: USD = THB / {EXCHANGE_RATE}")
    print(f"{amount:.2f} THB = {result:.2f} USD")
elif choice == "2":
    result = amount * EXCHANGE_RATE
    print(f"\nFormula: THB = USD * {EXCHANGE_RATE}")
    print(f"{amount:.2f} USD = {result:.2f} THB")
else:
    print("Invalid choice. Please enter 1 or 2.")