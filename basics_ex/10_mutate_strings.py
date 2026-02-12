string1 = input()
string2 = input()

for char_index in range(len(string1)):
    left_part = string2[:char_index + 1]
    right_part = string1[char_index + 1:]
    new_string = left_part + right_part
    if string1[char_index] != string2[char_index]:
        print(new_string)