prices = []

print("Enter prices of 6 items:")
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)

budget = int(input("\nEnter total budget: "))

total_spent = 0
bought_items = []

print()
for i in range(len(prices)):
    if total_spent + prices[i] <= budget:
        result = "buy"
        total_spent += prices[i]
        bought_items.append(prices[i])
    else:
        result = "cannot buy"

    print(f"Item {i + 1} = {prices[i]} -> {result}")
    print(f"Current total = {total_spent}\n")

print(f"Bought items: {bought_items}")
print(f"Total spent: {total_spent}")
print(f"Remaining budget: {budget - total_spent}")