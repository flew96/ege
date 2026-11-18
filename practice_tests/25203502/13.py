def f(start, stop):
    if start == stop:
        return 1
    elif start > stop:
        return 0
    
    moves = [
        f(start+1,stop)
    ]
    
    if str(start).count("1") >= 1:
        moves.append(f(int(str(start).replace("1", "3")), stop))
    
    return sum(moves)

print(f(10, 84))