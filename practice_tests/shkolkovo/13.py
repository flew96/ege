def f(start, stop, was_8=False, was_20=False):
    count = 0
    if start == stop:
        return (not (was_8 and was_20))
    elif start < stop:
        return 0
    if start == 8:
        was_8 = True
    if start == 20:
        was_20 = True
    
    moves = [
        f(start-1, stop, was_8, was_20),
        f(start-3, stop, was_8, was_20),
        f(start//2, stop, was_8, was_20)
    ]
    
    return sum(moves)

print(f(31, 3))