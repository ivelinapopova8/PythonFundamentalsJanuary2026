text = input()
text = text.lower()
i = 0

i += text.count("sand")
i += text.count("water")
i += text.count("fish")
i += text.count("sun")

print(i)