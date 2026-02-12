orders = int(input())
total = 0

for i in range(orders):
    costs = 0
    price = float(input())
    days = int(input())
    capsules_day = int(input())

    if not (0.01 <= price <= 100):
        continue
    if not (1 <= days <= 31):
        continue
    if not (1 <= capsules_day <= 2000):
        continue

    costs = price * capsules_day * days
    total += costs
    print(f"The price for the coffee is: ${costs:.2f}")

print(f"Total: ${total:.2f}")