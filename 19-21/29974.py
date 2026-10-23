# def f19(s, step=1): #1p 2v 3p 
#     if (s <= 15) and (step == 3):
#         return True
#     elif (
#         ((s <= 15) and (step < 3)) or
#         ((s > 15) and step == 3)
#     ):
#         return False
    
#     moves = [
#         f19(s-3, step + 1),
#         f19(s-7, step + 1),
#         f19(s // 4, step + 1)
#     ]
    
#     if step % 2 == 0:
#         return any(moves)
#     return all(moves)

# for s in range(16, 10000):
#     if f19(s):
#         print(s)
#         break

# def f20(s, step=1): #1p 2v 3p 
#     if (s <= 15) and (step == 4):
#         return True
#     elif (
#         ((s <= 15) and (step < 4)) or
#         ((s > 15) and step == 4)
#     ):
#         return False
    
#     moves = [
#         f20(s-3, step + 1),
#         f20(s-7, step + 1),
#         f20(s // 4, step + 1)
#     ]
    
#     if step % 2 == 0:
#         return all(moves)
#     return any(moves)

# for s in range(16, 10000):
#     if f20(s):
#         print(s)

def f21(s, step=1): #1p 2v 3p 
    if (s <= 15) and (step in (3,)):
        return True
    elif (
        ((s <= 15) and (step < 3)) or
        ((s > 15) and step == 3)
    ):
        return False
    
    moves = [
        f21(s-3, step + 1),
        f21(s-7, step + 1),
        f21(s // 4, step + 1)
    ]
    
    if step % 2 == 0:
        return any(moves)
    return all(moves)

for s in range(16, 10000):
    if f21(s):
        print(s)
        

70
74
75
76
268
269
270