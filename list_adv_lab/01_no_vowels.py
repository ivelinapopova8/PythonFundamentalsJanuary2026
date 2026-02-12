text = input()
sorted_text = [ch for ch in text if ch.lower() not in 'aeiou']
print("".join(sorted_text))