def f19(s1, s2, step=1):
    if (s1 + s2 >= 154) and (step in (3,)):
        return True
    elif (
        ((s1 + s2 >= 154) and (step < 3)) or
        ((s1 + s2 < 154) and step == 3)
    ):
        return False
    
    moves = [
        f19(s1 + 4, s2, step + 1),
        f19(s1, s2 + 4, step + 1),
        f19(s1*3, s2, step + 1),
        f19(s1, s2*3, step + 1)
    ]
    
    if step % 2 == 0:
        return any(moves)
    return all(moves)

for s2 in range(1, 143):
    if f19(11, s2):
        print(s2)
        
41
42
44