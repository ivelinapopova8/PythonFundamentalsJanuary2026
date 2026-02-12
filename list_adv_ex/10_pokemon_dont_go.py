distances = list(map(int,input().split()))
sum_removed = 0

while distances:
    index = int(input())

    if index < 0:
        removed = distances.pop(0)
        sum_removed += removed
        distances.insert(0, distances[-1])
    elif index > len(distances)-1:
        removed = distances.pop(-1)
        sum_removed += removed
        distances.append(distances[0])
    else:
        removed = distances.pop(index)
        sum_removed += removed

    for i in range (len(distances)):
        if distances[i] <= removed:
            distances[i] += removed
        else:
            distances[i] -= removed

print(sum_removed)