string = input()
numbers = []
non_numbers = []

for ch in string:
    if ch.isdigit():
        numbers.append(ch)
    else:
        non_numbers.append(ch)

take_list = []
skip_list = []

for i in range(len(numbers)):
    if i % 2 == 0:
        take_list.append(int(numbers[i]))
    else:
        skip_list.append(int(numbers[i]))

result = ""
current_index = 0
for i in range(len(take_list)):
    take = int(take_list[i])
    skip = int(skip_list[i])

    result += "" .join(non_numbers[current_index: current_index + take])
    current_index += take
    current_index += skip

print(result)

