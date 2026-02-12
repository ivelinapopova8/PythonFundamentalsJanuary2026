numbers_ = input().split()
numbers_ = list(map(int, numbers_))

def sorted_nums(numbers):
    return sorted(numbers)

print(sorted_nums(numbers_))