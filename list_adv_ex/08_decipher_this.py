secret_message = input().split()
result = ""

for word in secret_message:
    num_str = ""
    for char in word:
        if char.isdigit():
            num_str += char
        else:
            break
    first_letter = chr(int(num_str))
    rest_word = word[len(num_str):]
    decoded_word = first_letter + rest_word
    if len(decoded_word) > 2:
        chars = list(decoded_word)
        chars[1], chars[-1] = chars[-1], chars[1]
        decoded_word = "".join(chars)

    result += decoded_word + " "

print(result.strip())