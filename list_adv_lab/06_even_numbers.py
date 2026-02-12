numbers = list(map(int, input().split(", ")))
even_indices = []
for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        even_indices.append(i)
print(even_indices)