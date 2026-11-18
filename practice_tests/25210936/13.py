def f(start, stop):
    if start == stop:
        return 1
    elif start < stop or start == 17:
        return 0
    
    moves = [
        f(start-1, stop),
        f(start-3, stop),
        f(start//2, stop)
    ]
    
    return sum(moves)

print(f(29, 13)*f(13, 5))