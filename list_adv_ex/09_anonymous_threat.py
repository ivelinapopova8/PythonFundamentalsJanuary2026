strings = input().split()

while True:
    current_command = input()

    if "3:1" in current_command:
        break

    if "merge" in current_command:
        command, start, end = current_command.split()
        start_index = int(start)
        end_index = int(end)
        start_index = max(0, start_index)
        end_index = min(len(strings)-1, end_index)
        merged = "" .join(strings[start_index:end_index+1])
        strings = strings[:start_index] +[merged] + strings[end_index + 1:]

    elif "divide" in current_command:
        command, index_str, partitions_str = current_command.split()
        index = int(index_str)
        partitions = int(partitions_str)
        word = strings[index]
        part_length = len(word) // partitions
        reminder = len(word) % partitions
        current = 0
        new_parts = []
        for i in range(partitions):
            if i == partitions - 1:
                new_parts.append(word[current:])
            else:
                new_parts.append(word[current:current+part_length])
                current += part_length
        strings = strings[:index] + new_parts + strings[index+1:]

print(" ".join(strings))