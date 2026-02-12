string = input()

wolf_index = string.find("wolf")
after_wolf = string[wolf_index + len("wolf"):]
N = after_wolf.count("sheep")

if N == 0:
    print(f"Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {N}! You are about to be eaten by a wolf!")