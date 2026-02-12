version = list(map(int, input().split(".")))

num1, num2, num3 = version[0], version[1], version[2]

if num3 == 9:
    num3 = 0
    if num2 == 9:
        num2 =0
        num1 += 1
    else:
        num2 += 1
else:
    num3 += 1

new_version = [str(num1), str(num2), str(num3)]
print(".".join(new_version))
