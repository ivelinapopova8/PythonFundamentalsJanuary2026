coffees = 0
while True:
    command = input()
    if command == "END":
        break

    if not ((command.lower() == "coding") or (command.lower() == "dog") or (command.lower() == "cat") or (command.lower() == "movie")):
        continue

    if command.isupper():
        coffees += 2
    else:
        coffees += 1

if coffees > 5:
    print(f"You need extra sleep")
else:
    print(coffees)