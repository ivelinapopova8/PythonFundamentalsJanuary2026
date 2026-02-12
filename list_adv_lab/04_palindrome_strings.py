from itertools import count

words = input().split()
palindrome = input()

palindrome_list = [word for word in words if word == word[::-1]]
count_palindrome = palindrome_list.count(palindrome)

print(palindrome_list)
print(f"Found palindrome {count_palindrome} times")
