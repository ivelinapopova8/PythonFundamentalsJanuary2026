def sum_numbers(num1, num2):
    return num1 + num2

def subtract(sum_result, num3):
    return sum_result - num3

def add_and_subtract(num1, num2, num3):
    sum_result = sum_numbers(num1, num2)
    result = subtract(sum_result, num3)
    return result

num1_ = int(input())
num2_ = int(input())
num3_ = int(input())

print(add_and_subtract(num1_, num2_, num3_))
