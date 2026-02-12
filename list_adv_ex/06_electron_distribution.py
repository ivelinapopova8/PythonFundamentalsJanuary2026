electrons = int(input())
shels = []
n = 1

while electrons > 0:
    max_fill = 2 * (n ** 2)
    if max_fill > electrons:
        shels.append(electrons)
        break
    else:
        shels.append(max_fill)
        electrons -= max_fill

    n += 1

print(shels)