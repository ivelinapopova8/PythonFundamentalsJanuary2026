def multiply_result(num1, num2, num3):
    negatives = 0
    if num1 < 0:
        negatives += 1
    if num2 < 0:
        negatives += 1
    if num3 < 0:
        negatives += 1

    if num1 == 0 or num3 == 0 or num2 == 0:
        return "zero"
    elif negatives % 2 != 0:
        return "negative"
    else:
        return "positive"

a = int(input())
b = int(input())
c = int(input())
print(multiply_result(a, b, c))