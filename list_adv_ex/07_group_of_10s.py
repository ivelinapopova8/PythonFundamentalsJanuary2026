numbers = list(map(int, input().split(", ")))
max_num = max(numbers)
max_group = ((max_num + 9)//10)* 10
current_group = 10

while current_group <= max_group:
    group = [x for x in numbers if current_group - 10 < x <= current_group]
    print(f"Group of {current_group}'s: {group}")
    current_group += 10