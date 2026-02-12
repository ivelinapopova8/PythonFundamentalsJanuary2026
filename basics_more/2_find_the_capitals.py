text = input()
i = 0
result = "["

for char in text:
    if char.isupper():
        if result != "[":
            result += ", "
        result += str(i)
    i += 1

result += "]"
print(result)
