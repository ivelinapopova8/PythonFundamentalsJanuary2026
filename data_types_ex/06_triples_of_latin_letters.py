num = int(input())

for first_num in range(97, 97 + num):
    for second_num in range(97, 97 + num):
        for third_num in range(97, 97 + num):
            print(f"{chr(first_num)}{chr(second_num)}{chr(third_num)}")