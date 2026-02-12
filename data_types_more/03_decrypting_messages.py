key = int(input())
lines = int(input())
result = ""
for i in range(lines):
    letter = input()

    new_symbol = chr(ord(letter) + key)
    result += new_symbol

print(result)