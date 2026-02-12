def data_type(type, number):
    if type == "int":
        number = int(number)
        print(number * 2)
    elif type == "real":
        number = float(number)
        print(f"{number * 1.5:.2f}")
    elif type == "string":
        print(f"${number}$")

type_ = input()
number_ = input()
data_type(type_, number_)