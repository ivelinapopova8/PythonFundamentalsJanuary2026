numbers_ = input().split()
numbers_ = list(map(int, numbers_))

def even_numbers(numbers_):
    numbers_even = list(filter(lambda x: x % 2 == 0, numbers_ ))
    return numbers_even

print(even_numbers(numbers_))