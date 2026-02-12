while True:
    string = input()

    if string == "SoftUni":
        continue

    if string == "End":
        break

    result = ""

    for char in string:
        result += char*2

    print(result)
