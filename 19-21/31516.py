# def f19(s1, s2, step=1): #1p 2v 3p 4v 5p
#     if (s1 + s2 >= 133) and (step == 3):
#         return True
#     elif (
#         ((s1 + s2 >= 133) and (step < 3)) or
#         ((s1 + s2 < 133) and (step == 3))
#     ):
#         return False
    
#     moves = [
#         f19(s1 + 4, s2, step + 1),
#         f19(s1, s2 + 4, step + 1),
#         f19(s1*2, s2, step + 1),
#         f19(s1, s2*2, step + 1)
#     ]
    
#     if step % 2 == 0: # ваня - четные ходы
#         return any(moves)
#     return any(moves)

# for s2 in range(1, 116):
#     if f19(17, s2):
#         print(s2)
#         break

# def f20(s1, s2, step=1): #1p 2v 3p 4v 5p
#     if (s1 + s2 >= 133) and (step == 4):
#         return True
#     elif (
#         ((s1 + s2 >= 133) and (step < 4)) or
#         ((s1 + s2 < 133) and (step == 4))
#     ):
#         return False
    
#     moves = [
#         f20(s1 + 4, s2, step + 1),
#         f20(s1, s2 + 4, step + 1),
#         f20(s1*2, s2, step + 1),
#         f20(s1, s2*2, step + 1)
#     ]
    
#     if step % 2 == 0: # ваня - четные ходы
#         return all(moves)
#     return any(moves)

# for s2 in range(1, 116):
#     if f20(17, s2):
#         print(s2)

def f21(s1, s2, step=1): #1p 2v 3p 4v 5p
    if (s1 + s2 >= 133) and (step in (3,)):
        return True
    elif (
        ((s1 + s2 >= 133) and (step < 3)) or
        ((s1 + s2 < 133) and (step == 3))
    ):
        return False
    
    moves = [
        f21(s1 + 4, s2, step + 1),
        f21(s1, s2 + 4, step + 1),
        f21(s1*2, s2, step + 1),
        f21(s1, s2*2, step + 1)
    ]
    
    if step % 2 == 0: # ваня - четные ходы
        return any(moves)
    return all(moves)

for s2 in range(1, 116):
    if f21(17, s2):
        print(s2)
        
44
45
50
51

