# def f19(s1, s2, step=1): #1p #2v #3p
#     if (s1 + s2 <= 53) and (step == 3):
#         return True
#     elif (
#         ((s1 + s2 > 53) and (step == 3)) or
#         (s1 + s2 <= 53) and (step < 3)
#     ):
#         return False
    
#     moves = [
#         f19(s1-3, s2, step+1),
#         f19(s1, s2-3, step+1),
#         f19(s1 // 3, s2, step+1),
#         f19(s1, s2 // 3, step+1)
#     ]
    
#     #! ПОБЕДИТЕЛЬ ВСЕГДА any()
#     #! ПРОИГРАВШИЙ all() если любой ход/независимо от стратегии...
#     #! ПРОИГРАВШИЙ any() когда НЕУДАЧНЫЙ ХОД
    
#     if step % 2 == 0:
#         return any(moves)
#     return any(moves)

# for s2 in range(35, 10000):
#     if f19(19, s2):
#         print(s2)
#         break


# def f20(s1, s2, step=1): #1p #2v #3p
#     if (s1 + s2 <= 53) and (step == 4):
#         return True
#     elif (
#         ((s1 + s2 > 53) and (step == 4)) or
#         (s1 + s2 <= 53) and (step < 4)
#     ):
#         return False
    
#     moves = [
#         f20(s1-3, s2, step+1),
#         f20(s1, s2-3, step+1),
#         f20(s1 // 3, s2, step+1),
#         f20(s1, s2 // 3, step+1)
#     ]
    
#     #! ПОБЕДИТЕЛЬ ВСЕГДА any()
#     #! ПРОИГРАВШИЙ all() если любой ход/независимо от стратегии...
#     #! ПРОИГРАВШИЙ any() когда НЕУДАЧНЫЙ ХОД
    
#     if step % 2 == 0:
#         return all(moves)
#     return any(moves)

# for s2 in range(35, 10000):
#     if f20(19, s2):
#         print(s2)
        

# # 108 323

def f21(s1, s2, step=1): #1p #2v #3p
    if (s1 + s2 <= 53) and (step in (3,)):
        return True
    elif (
        ((s1 + s2 > 53) and (step == 3)) or
        (s1 + s2 <= 53) and (step < 3)
    ):
        return False
    
    moves = [
        f21(s1-3, s2, step+1),
        f21(s1, s2-3, step+1),
        f21(s1 // 3, s2, step+1),
        f21(s1, s2 // 3, step+1)
    ]
    
    #! ПОБЕДИТЕЛЬ ВСЕГДА any()
    #! ПРОИГРАВШИЙ all() если любой ход/независимо от стратегии...
    #! ПРОИГРАВШИЙ any() когда НЕУДАЧНЫЙ ХОД
    
    if step % 2 == 0:
        return any(moves)
    return all(moves)

for s2 in range(35, 10000):
    if f21(19, s2):
        print(s2)
        

111
112
113
117
118
119
147
148
149