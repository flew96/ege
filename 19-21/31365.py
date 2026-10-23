# def f19(s1, s2, step=1): #1p 2v 3p 
#     if (s1 + s2 <= 47)  and (step == 3):
#         return True
#     elif (
#         (s1 + s2 <= 47) and (step < 3) or
#         (s1 + s2 > 47) and (step == 3)
#     ):
#         return False
    
#     moves = [
#         f19(s1 - 2, s2, step + 1),
#         f19(s1, s2 - 2, step + 1),
#         f19(s1 // 3, s2, step + 1),
#         f19(s1, s2 // 3, step + 1)
#     ]
    
#     if step % 2 == 0:
#         return any(moves)
#     return any(moves)

# for s2 in range(32, 10000):
#     if f19(16, s2):
#         print(s2)
#         break


# def f20(s1, s2, step=1): #1p 2v 3p 
#     if (s1 + s2 <= 47)  and (step == 4):
#         return True
#     elif (
#         (s1 + s2 <= 47) and (step < 4) or
#         (s1 + s2 > 47) and (step == 4)
#     ):
#         return False
    
#     moves = [
#         f20(s1 - 2, s2, step + 1),
#         f20(s1, s2 - 2, step + 1),
#         f20(s1 // 3, s2, step + 1),
#         f20(s1, s2 // 3, step + 1)
#     ]
    
#     if step % 2 == 0:
#         return all(moves)
#     return any(moves)

# for s2 in range(32, 10000):
#     if f20(16, s2):
#         print(s2)

def f21(s1, s2, step=1): #1p 2v 3p 4v
    if (s1 + s2 <= 47)  and (step in (3,)):
        return True
    elif (
        (s1 + s2 <= 47) and (step < 3) or
        (s1 + s2 > 47) and (step == 3)
    ):
        return False
    
    moves = [
        f21(s1 - 2, s2, step + 1),
        f21(s1, s2 - 2, step + 1),
        f21(s1 // 3, s2, step + 1),
        f21(s1, s2 // 3, step + 1)
    ]
    
    if step % 2 == 0:
        return any(moves)
    return all(moves)

for s2 in range(32, 10000):
    if f21(16, s2):
        print(s2)
        
100
101
104
105
132