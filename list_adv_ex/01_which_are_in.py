str1 = input().split(", ")
str2 = input().split(", ")

str3 = []

for word in str1:
    is_there = False
    for sent in str2:
        if word in sent:
            is_there = True
    if is_there:
        str3.append(word)


print(str3)