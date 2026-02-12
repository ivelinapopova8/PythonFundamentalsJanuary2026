def loading_bar(number):
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        num_percent = number // 10
        num_dots = 10 - (number // 10)
        bar = "[" + "%" * num_percent + "." * num_dots + "]"
        print(str(number) + "%" " "+ bar)
        print("Still loading...")


number_ = int(input())
loading_bar(number_)

