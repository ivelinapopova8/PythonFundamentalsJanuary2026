def office_happiness(lst_happiness, factor):
    multy_happiness = [x * factor for x in lst_happiness]
    average_happiness = sum(multy_happiness) / len(multy_happiness)
    happy_count = sum(num >= average_happiness for num in multy_happiness)
    return happy_count

lst_happiness_ = list(map(int, input().split()))
factor_ = int(input())
happy = office_happiness(lst_happiness_, factor_)
if happy >= len(lst_happiness_) / 2:
    print(f"Score: {happy}/{len(lst_happiness_)}. Employees are happy!")
else:
    print(f"Score: {happy}/{len(lst_happiness_)}. Employees are not happy!")

