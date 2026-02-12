is_good = False

while True:
    name = input()

    if name == "Voldemort":
        print(f"You must not speak of that name!")
        break

    if name == "Welcome!":
        is_good = True
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

if is_good:
    print(f"Welcome to Hogwarts.")