number_ = input()

def number_function(number):
    sum_even = 0
    sum_odd = 0
    for dig in number:
        num = int(dig)
        if num % 2 == 0:
            sum_even += num
        elif num % 2 == 1:
            sum_odd += num

    return sum_even, sum_odd

sum_even_ , sum_odd_ = number_function(number_)
print(f"Odd sum = {sum_odd_}, Even sum = {sum_even_}")