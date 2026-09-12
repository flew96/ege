def f(start, stop):
    if start == stop:
        return 1
    if start > stop or start == 16:
        return 0
    
    moves = [f(start + 1, stop), 
             f(start* 3, stop),
             f(start + 5, stop)]
    
    return sum(moves)

print(f(2, 7) * f(7, 21))