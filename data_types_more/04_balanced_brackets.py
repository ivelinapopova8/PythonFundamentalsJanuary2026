lines = int(input())
opened = False
balanced = True

for i in range(lines):
    str = input()
    if str == "(":
        if opened:
            balanced = False
            break
        opened = True
    elif str == ")":
        if not opened:
            balanced = False
            break
        opened = False
    else:
        continue

if balanced and not opened:
    print("BALANCED")
else:
    print("UNBALANCED")

