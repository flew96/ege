def f(start, stop):
    if start == stop:
        return 1
    elif start < stop or start == 10:
        return 0

    moves = [
        f(start-1, stop),
        f(start//3, stop)
    ]

    return sum(moves)

print(f(64,21)*f(21,4))
#answ = 30