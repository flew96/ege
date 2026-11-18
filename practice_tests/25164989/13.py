def f(start, stop):
    if start == stop:
        return 1
    elif start < stop:
        return 0
    
    moves = [
        f(start - 1, stop),
        f(start//2, stop)
    ]
    
    return sum(moves)

print(f(40, 16) * f(16, 6))