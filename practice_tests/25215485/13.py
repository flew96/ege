def f(start, stop):
    if start == stop:
        return 1
    elif start > stop or start == 10:
        return 0

    moves = [
        f(start+1, stop),
        f(start*2, stop),
        f(start*3, stop)
    ]

    return (sum(moves))

print(f(2, 20)*f(20, 30))
print(54 + 29)