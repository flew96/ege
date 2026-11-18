def f(start, stop):
    if start == stop:
        return 1
    elif start < stop or start == 70:
        return 0

    moves = [
        f(start-4, stop),
        f(start-9, stop),
        f(start//2, stop)
    ]

    return sum(moves)

print(f(91, 50)*f(50, 8))