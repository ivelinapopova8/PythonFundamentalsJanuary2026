numbers = input().split()
round_numbers = []

for num in numbers:
    round_numbers.append(round(float(num)))

print(round_numbers)