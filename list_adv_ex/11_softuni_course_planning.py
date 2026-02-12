lessons = input().split(", ")

while True:
    commands = input()
    if commands == "course start":
        break

    if "Add" in commands:
        command, lesson = commands.split(":")
        if lesson not in lessons:
            lessons.append(lesson)

    elif "Insert" in commands:
        command, lesson, index = commands.split(":")
        index = int(index)
        if lesson not in lessons:
            lessons.insert(index, lesson)

    elif "Remove" in commands:
        command, lesson = commands.split(":")
        if lesson in lessons:
            lessons.remove(lesson)
            ex = f"{lesson}-Exercise"
            if ex in lessons:
                lessons.remove(ex)

    elif "Swap" in commands:
        command, lesson1, lesson2 = commands.split(":")
        if lesson1 in lessons and lesson2 in lessons:
            idx1, idx2 = lessons.index(lesson1), lessons.index(lesson2)
            lessons[idx1], lessons[idx2] = lessons[idx2], lessons[idx1]

        ex1 = f"{lesson1}-Exercise"
        if ex1 in lessons:
            lessons.remove(ex1)
            idx1_new = lessons.index(lesson1)
            lessons.insert(idx1_new + 1, ex1)

        ex2 = f"{lesson2}-Exercise"
        if ex2 in lessons:
            lessons.remove(ex2)
            idx2_new = lessons.index(lesson2)
            lessons.insert(idx2_new + 1, ex2)

    elif "Exercise" in commands:
        command, lesson = commands.split(":")
        ex = f"{lesson}-Exercise"
        if lesson in lessons:
            if ex not in lessons:
                lessons.insert(lessons.index(lesson)+1, ex)
        else:
            lessons.append(lesson)
            lessons.append(ex)

for i, lesson in enumerate(lessons, start=1):
    print(f"{i}.{lesson}")
