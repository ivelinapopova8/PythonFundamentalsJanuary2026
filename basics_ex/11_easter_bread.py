budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = 0.75 * price_1kg_flour
price_1l_milk = 1.25 * price_1kg_flour

breads = 0
eggs = 0

while True:
    need_money = price_1pack_eggs +price_1kg_flour + 0.25 * price_1l_milk

    if need_money > budget:
        break
    else:
        budget -= need_money

    breads += 1
    eggs += 3
    if breads % 3 == 0:
        eggs -= breads - 2

print(f"You made {breads} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")