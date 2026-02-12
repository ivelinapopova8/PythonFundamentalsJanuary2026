from math import floor

def center_point(x1, y1, x2, y2):
    d1 = (x1 ** 2) + (y1 ** 2)
    d2 = (x2 ** 2) + (y2 ** 2)

    if d1 <= d2:
        return floor(x1), floor(y1)
    elif d2 <= d1:
        return floor(x2), floor(y2)

x1_ = float(input())
y1_ = float(input())
x2_ = float(input())
y2_ = float(input())
x, y = center_point(x1_, y1_, x2_, y2_)
print(f"({x}, {y})")
