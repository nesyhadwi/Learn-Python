def square_root(number):
    x = number
    while True:
        y = (x + number / x) / 2
        if y == x:
            return int(y)
        x = y