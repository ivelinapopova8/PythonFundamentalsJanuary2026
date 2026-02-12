string = input().split(", ")
new_lst = []

for i in string:
    number = int(i)

    if number == 0:
        string.remove(i)
        string.append(i)

for t in string:
    num = int(t)
    new_lst.append(num)

print(new_lst)