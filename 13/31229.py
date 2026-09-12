def f(start, stop):
    if start == stop:
        return 1
    if start > stop:
        return 0

    moves = [
        f(start + 1, stop)
        
    ]