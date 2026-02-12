start = int(input())
end = int(input())
result = ""

for num in range(start, end + 1):
    result += chr(num) + " "

print(result)