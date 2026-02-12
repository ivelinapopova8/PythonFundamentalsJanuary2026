def factorial_numbers(num1, num2):
    factorial1 = 1
    factorial2 = 1
    for i in range(1, num1 + 1):
        factorial1 = factorial1 * i
    for t in range(1, num2 + 1):
        factorial2 = factorial2 * t

    result = factorial1 / factorial2
    return result

num1_ = int(input())
num2_ = int(input())
print(f"{factorial_numbers(num1_, num2_):.2f}")
