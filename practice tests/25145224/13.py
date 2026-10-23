def f(start, stop):
    if start == stop:
        return 1
    if start < stop or start == 26:
        return 0

    moves = [
        f(start-4, stop),
        f(start-7, stop),
        f(start//3, stop)
    ]

    return sum(moves)

print(f(91, 41) * f(41, 14))