from math import floor

def lines(x1, y1, x2, y2, x3, y3, x4, y4):
    lengh_line1 = (x1 - x2)**2 + (y1 - y2)**2
    lengh_line2 = (x3 - x4)**2 + (y3 - y4)**2

    if lengh_line1 >= lengh_line2:
        d1 = x1 ** 2 + y1 ** 2
        d2 = x2 ** 2 + y2 ** 2
        if d1 >= d2:
            return x1,y1,x2,y2
        else:
            return x2, y2, x1, y1
    else:
        d3 = x3 ** 2 + y3 ** 2
        d4 = x4 ** 2 + y4 ** 2
        if d3 <= d4:
            return x3, y3, x4, y4
        else:
            return x4, y4, x3, y3

x1_ = float(input())
y1_ = float(input())
x2_ = float(input())
y2_ = float(input())
x3_ = float(input())
y3_ = float(input())
x4_ = float(input())
y4_ = float(input())

x_short, y_short, x, y = lines(x1_, y1_, x2_, y2_, x3_, y3_, x4_, y4_)
print(f"({floor(x_short)}, {floor(y_short)})({floor(x)}, {floor(y)})")