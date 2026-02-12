population = list(map(int, input().split(", ")))
minimum = int(input())
all_need = 0

for human in population:
    if human < minimum:
        all_need += minimum - human

total_wealth = sum(population)
min_need = minimum * len(population)

if total_wealth < min_need:
    print("No equal distribution possible")
    exit()
else:
    while min(population) < minimum:
        min_value = min(population)
        min_index = population.index(min_value)
        needed = minimum - population[min_index]
        available = population[-1] - minimum
        if available >= needed:
            population[min_index] += needed
            population[-1] -= needed
        else:
            population[min_index] += available
            population[-1] -= available
            need_more = minimum - population[min_index]

            for i in range(len(population)-1, -1, -1):
                available = population[i] - minimum
                if available <= 0:
                    continue
                take = min(available, need_more)
                population[i] -= take
                population[min_index] += take
                need_more -= take
                if need_more == 0:
                    break
            if need_more > 0:
                print("No equal distribution possible")
                exit()
print(population)