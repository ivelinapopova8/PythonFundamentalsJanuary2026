characteres = []

def characters_between(char1, char2):
    for char_in in range(ord(char1) + 1, ord(char2)):
        characteres.append(chr(char_in))
    return characteres

char1_ = input()
char2_ = input()

result = characters_between(char1_, char2_)
print(" ".join(result))
