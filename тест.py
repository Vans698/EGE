# 2
# print('x y w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 f = (w == z) or not(y <= w) or not(x)
#                 if f == 0:
#                     print(x, y, w, z)

# 5
# def eght(x):
#     s = ''
#     while x != 0:
#         s = str(x%8) + s
#         x//=8
#     return s

# for n in range(8, 1000):
#     n8 = eght(n)
#     if int(n8)%2 == 0:
#         n8 += n8[-1]
#     else:
#         n8 = n8[-1] + n8[1:-1] + n8[0]
#     if int(n8, 8) < 254:
#         print(n)

# 6
# from turtle import *
# tracer(0)
# screensize(3000, 3000)
# c = 25
# lt(90)

# down()
# rt(45)

# for i in range(3):
#     rt(45)
#     fd(10*c)
#     rt(45)

# rt(315)
# fd(10*c)
# rt(90)
# fd(20*c)
# rt(90)

# for i in range(2):
#     fd(10*c)
#     rt(90)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*c, y*c)
#         if x == 0 or y == 0:
#             dot(5, 'red')
#         else:
#             dot(5, 'blue')

# update()
# exitonclick()

# 8
# from itertools import product
# k = 0
# for x in product('АЕЛПРЬ', repeat=5):
#     k += 1
#     s = ''.join(x)
#     if k%2 == 0  and s[0] != 'Ь' and s[0] != 'Р' and s.count('Л') >= 2:
#         print(k)

# 9
# with open('9.txt') as f:
#     k = 0
#     for i in f:
#         k += 1
#         m = [int(x) for x in i.split()]
#         m1 = []
#         m2 = []
#         for j in m:
#             if m.count(j) == 1:
#                 m1.append(j)
#             if m.count(j) == 3:
#                 m2.append(j)
#         if len(m1) == 4 and len(m2) == 3 and (max(m) in m2) and (max(m)%10 == 0):
#             print(k)
#             break

# 14

# c = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')[:23]
# for x in (''.join(c)):
#     b = int(f'324{x}72', 23) + int(f'45{x}562', 23)
#     if b%22 == 0:
#         print(b//22)
#         break

# 15

# def f(x, la, ra):
#     return not((75 <= x <= 185) <= ((not(la <= x <= ra) and (19 <= x <= 142)) <= (not(75 <= x <= 185))))

# for la in range(300):
#     for ra in range(la, 300):
#         if not any([f(x+0.5, la, ra) for x in range(300)]):
#             print(ra - la)
#             break

# 17

# with open('17.txt') as f:
#     s = [int(x) for x in f]

#     m = []
#     for i in s:
#         if abs(i)%25 == 0:
#             m.append(i)
#     b = min(m)

#     k = []
#     for n in range(len(s) - 1):
#         c = (s[n]%2 == 0) + (s[n+1]%2 == 0)
#         a = s[n] + s[n+1]
#         if c >= 1 and a%b == 0:
#             k.append(a)

#     print(len(k), max(k))

# 19-21
# def f(s1, s2, m):
#     if s1 + s2 >= 154: return m%2 == 0
#     if m == 0: return 0
#     h = [f(s1+4, s2, m-1), f(s1, s2+4, m-1), f(s1*3, s2, m-1), f(s1, s2*3, m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# # print([s2 for s2 in range(1, 143) if f(11, s2, 2)])
# print(*[s2 for s2 in range(1, 143) if f(11, s2, 3) and not(f(11, s2, 1))])
# print(*[s2 for s2 in range(1, 143) if f(11, s2, 4) and not(f(11, s2, 2))])


# 23

# def f(x, y):
#     if x == y:
#         return 1
#     if x > y or x == 7:
#         return 0
#     return f(x+1, y) + f(x+3, y) + f(x*2, y)

# print(f(2, 15)*f(15, 25))