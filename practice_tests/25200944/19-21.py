# def f19(s1, s2, step=1):
#     if (s1 + s2 >= 167) and step == 3:
#         return 1
#     elif (s1 + s2 >= 167 and step < 3) or (s1 + s2 < 167 and step == 3):
#         return 0

#     moves = [
#         f19(s1 + 5, s2, step+1),
#         f19(s1, s2 + 5, step+1),
#         f19(s1*3, s2, step+1),
#         f19(s1, s2*3, step+1)
#     ]

#     if step % 2 == 0:
#         return any(moves)
#     return any(moves)

# for s2 in range(1, 155):
#     if f19(12, s2):
#         print(s2)
#         break

def f20(s1, s2, step=1): #1p 2v 3p 4v
    if (s1 + s2 >= 167) and step in (3,):
        return 1
    elif (s1 + s2 >= 167 and step < 3) or (s1 + s2 < 167 and step == 3):
        return 0

    moves = [
        f20(s1 + 5, s2, step+1),
        f20(s1, s2 + 5, step+1),
        f20(s1*3, s2, step+1),
        f20(s1, s2*3, step+1)
    ]

    if step % 2 == 0:
        return any(moves) #vanya
    return all(moves) #petya

for s2 in range(1, 155):
    if f20(12, s2):
        print(s2)

44
47
48
