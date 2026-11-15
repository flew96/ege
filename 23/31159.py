def f(start, stop):
    if start == stop:
        return 1
    if start > stop:
        return 0
    
    moves = [
        f(start+1, stop),
    ]
    
    if str(start).count("1") > 0:
        moves.append(
            f(int(str(start).replace("1", "2")), stop)
        )
    return sum(moves)

print(f(11,92))