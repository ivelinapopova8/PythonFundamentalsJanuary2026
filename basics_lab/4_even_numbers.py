n = int(input())
is_odd = False

for _ in range(n):
    num = int(input())

    if num % 2 != 0:
        is_odd = True
        print(f"{num} is odd!")
        break

if not is_odd:
    print(f"All numbers are even.")