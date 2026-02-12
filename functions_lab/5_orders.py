def price(order, quantity):
    if order == "coffee":
        return 1.50 * quantity
    elif order == "water":
        return 1.00 * quantity
    elif order == "coke":
        return 1.40 * quantity
    elif order == "snacks":
        return 2.00 * quantity

order_ = input()
quantity_ = int(input())
result = price(order_, quantity_)
print(f"{result:.2f}")
