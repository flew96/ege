# def f19(s1, s2, step=1): #1p #2v #3p #4v 
#     if (s1 + s2 >= 166 and step == 3):
#         return 1
#     elif (s1 + s2 >= 166 and step < 3) or (s1 + s2 < 166 and step == 3):
#         return 0

#     moves = [
#         f19(s1+3, s2, step+1),
#         f19(s1, s2+3, step+1),
#         f19(s1*4, s2, step+1),
#         f19(s1, s2*4, step+1)
#     ]

#     #! ПОБЕДИТЕЛЬ ВСЕГДА any()
#     #! ПРОИГРАВШИЙ all() если любой ход/независимо от стратегии...
#     #! ПРОИГРАВШИЙ any() когда НЕУДАЧНЫЙ ХОД

#     if step % 2 == 0: #v
#         return any(moves)
#     return all(moves) #p

# for s2 in range(1, 159):
#     if f19(7, s2):
#         print(s2)
#* answ = 39

# def f20(s1, s2, step=1): #1p #2v #3p #4v 
#     if (s1 + s2 >= 166 and step == 4):
#         return 1
#     elif (s1 + s2 >= 166 and step < 4) or (s1 + s2 < 166 and step == 4):
#         return 0

#     moves = [
#         f20(s1+3, s2, step+1),
#         f20(s1, s2+3, step+1),
#         f20(s1*4, s2, step+1),
#         f20(s1, s2*4, step+1)
#     ]

#     #! ПОБЕДИТЕЛЬ ВСЕГДА any()
#     #! ПРОИГРАВШИЙ all() если любой ход/независимо от стратегии...
#     #! ПРОИГРАВШИЙ any() когда НЕУДАЧНЫЙ ХОД

#     if step % 2 == 0: #v
#         return all(moves)
#     return any(moves) #p

# for s2 in range(1, 159):
#     if f20(7, s2):
#         print(s2)
# #* answ = 34, 36

def f21(s1, s2, step=1): #1p #2v #3p #4v 
    if (s1 + s2 >= 166 and step in (3,)):
        return 1
    elif (s1 + s2 >= 166 and step < 3) or (s1 + s2 < 166 and step in (3,)):
        return 0

    moves = [
        f21(s1+3, s2, step+1),
        f21(s1, s2+3, step+1),
        f21(s1*4, s2, step+1),
        f21(s1, s2*4, step+1)
    ]

    #! ПОБЕДИТЕЛЬ ВСЕГДА any()
    #! ПРОИГРАВШИЙ all() если любой ход/независимо от стратегии...
    #! ПРОИГРАВШИЙ any() когда НЕУДАЧНЫЙ ХОД

    if step % 2 == 0: 
        return any(moves) #v
    return all(moves) #p

for s2 in range(1, 159):
    if f21(7, s2):
        print(s2)

#* answ = 39 
#TODO: спросить!