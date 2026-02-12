num_snowballs = int(input())
snowball_value_max = 0
weight_max = 0
time_max = 0
quality_max = 0

for ball in range(num_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight // time) ** quality

    if value > snowball_value_max:
        snowball_value_max = value
        weight_max = weight
        time_max = time
        quality_max = quality

print(f"{weight_max} : {time_max} = {snowball_value_max} ({quality_max})")