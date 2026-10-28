# def f19(s, step=1):
#     if (s <= 37) and (step == 3):
#         return True
#     elif (
#         (s > 37 and step == 3) or
#         (s <= 37 and step < 3)
#     ):
#         return False
    
#     moves =[
#         f19(s-2, step+1),
#         f19(s//2, step+1)
#     ]
    
#     if step % 2 == 0:
#         return any(moves)
#     return all(moves)

# for s in range(38, 1000):
#     if f19(s):
#         print(s)
#         break


# def f20(s, step=1):
#     if (s <= 37) and (step == 4):
#         return True
#     elif (
#         (s > 37 and step == 4) or
#         (s <= 37 and step < 4)
#     ):
#         return False
    
#     moves =[
#         f20(s-2, step+1),
#         f20(s//2, step+1)
#     ]
    
#     if step % 2 == 0:
#         return all(moves)
#     return any(moves)

# for s in range(38, 1000):
#     if f20(s):
#         print(s)
    

def f21(s, step=1):
    if (s <= 37) and (step in (3,)):
        return True
    elif (
        (s > 37 and step == 3) or
        (s <= 37 and step < 3)
    ):
        return False
    
    moves =[
        f21(s-2, step+1),
        f21(s//2, step+1)
    ]
    
    if step % 2 == 0:
        return any(moves)
    return all(moves)

for s in range(38, 1000):
    if f21(s):
        print(s)
        
76
77
80
81
156
157

