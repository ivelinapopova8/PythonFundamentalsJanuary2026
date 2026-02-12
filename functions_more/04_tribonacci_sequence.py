def tribonacci(num):
    tribonacci_list = [1, 1, 2]
    while len(tribonacci_list) < num:
        new_number = tribonacci_list[-1] + tribonacci_list[-2] + tribonacci_list[-3]
        tribonacci_list.append(new_number)
    return tribonacci_list[:num]


number = int(input())
print(*tribonacci(number))