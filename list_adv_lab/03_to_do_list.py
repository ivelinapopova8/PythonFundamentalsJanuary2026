lst = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    importance, note = command.split("-")
    index = int(importance) - 1

    lst[index] = note


final_lst = [sent for sent in lst if sent != 0]
print(final_lst)