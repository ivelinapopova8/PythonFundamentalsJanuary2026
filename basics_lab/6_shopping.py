budget = int(input())
is_enough = True

while True:
    price = input()

    if price == "End":
        break

    price = int(price)

    if price > budget:
        is_enough = False
        print(f"You went in overdraft!")
        break

    budget -= price

if is_enough:
    print(f"You bought everything needed.")
