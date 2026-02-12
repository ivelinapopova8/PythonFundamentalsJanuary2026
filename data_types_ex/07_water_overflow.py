capacity = 255
lines = int(input())
water_in = 0

for i in range(lines):
    liters = int(input())
    if liters > capacity:
        print(f"Insufficient capacity!")
        continue
    else:
        water_in += liters
        capacity -= liters

print(water_in)
