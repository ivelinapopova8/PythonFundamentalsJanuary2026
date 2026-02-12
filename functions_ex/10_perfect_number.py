def perfect_number(number):
    if sum(divisors) / 2 == number:
        return True
    else:
        return False

number_ = int(input())
divisors = []

for i in range(1, number_ + 1):
    if number_ % i == 0:
        divisors.append(i)

if perfect_number(number_):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")