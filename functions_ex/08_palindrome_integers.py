def palindrome(numbers):
    for num in numbers:
        if num[::-1] == num:
            print(True)
        else:
            print(False)

numbers_ = input().split(", ")

palindrome(numbers_)
