def f(start, stop):
    if start == stop:
        return 1
    elif start > stop:
        return 0
    
    moves = [
        f(start + 1, stop)
    ]
    if "1" in str(start):
        moves.append(
            f(int(str(start).replace("1", "3")), stop) )
    
    return sum(moves)

print(f(11, 94))