ORNAMENTS_SET = 2
TREE_SKIRT = 5
TREE_GARLAND = 3
TREE_LIGHTS = 15


quantity = int(input())
days_left = int(input())
days = 1
money = 0
points = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 3 == 0 and day % 5 == 0:
        points += 30

    if day % 2 == 0:
        money += ORNAMENTS_SET * quantity
        points += 5

    if day % 3 == 0:
        money += (TREE_SKIRT + TREE_GARLAND) * quantity
        points += 13

    if day % 5 == 0:
        money += TREE_LIGHTS * quantity
        points += 17

    if day % 10 == 0:
        points -= 20
        money += (TREE_LIGHTS + TREE_GARLAND + TREE_SKIRT)


if days_left % 10 == 0:
    points -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {points}")
