def f(start, stop):
    if start == stop:
        return 1
    elif start > stop or start == 16:
        return 0
    
    moves = [
        f(start + 1, stop),
        f(start + 3, stop),
        f(start**2, stop)
    ]
    
    return sum(moves)

print(f(3, 20) * f(20, 26))