# print('y x w z')
# for x in range(2):
#     for y in range(2):
#         for w in range(2):
#             for z in range(2):
#                 f = (z <= x) and ((not(y)) and ((not(w)) == y))
#                 if f == 0:
#                     print(y, x, w, z)

# for i in range(1000, 10_000):
#     s = str(i)
#     if (s.count('2') + s.count('4') + s.count('8')) == 0:
#         s = s.replace('3', '4').replace('7', '8')
#         r = 1
#         for m in s:
#             r*= int(m)
#         if r == 256:
#             print(i)
#             break

# from turtle import *
# screensize(3000, 3000)
# tracer(0)
# c=25
# lt(90)
# down()
# for _ in range(3):
#     fd(5*c)
#     rt(90)
#     fd(12*c)
#     rt(90)
# up()
# fd(3*c)
# rt(90)
# fd(2*c)
# rt(90)
# down()
# for _ in range(4):
#     fd(5*c)
#     rt(90)
#     fd(12*c)
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*c, y*c)
#         if x == 0 or y == 0:
#             dot(5, 'red')
#         else: dot(5, 'blue')
# update()
# exitonclick()

# from itertools import *
# k = 0
# for i in product('АВЕНС', repeat=5):
#     s = ''.join(i)
#     if s[0] == 'Н' and s.count('В') == 2:
#         if s.count('Н') == 1 and s.count('Е') <= 1 and s.count('С') <= 1 and s.count('А') <= 1:
#             k+=1
# print(k)


# with open('9.txt') as f:
#     k = 0
#     for i in f:
#         m = [int(x) for x in i.split()]
#         m1 = []
#         m2 = []
#         for j in m:
#             if m.count(j) == 2:
#                 m1.append(j)
#             if m.count(j) == 1:
#                 m2.append(j)
#         d = sum(m2) if len(m2) > 0 else 0
#         if len(set(m1)) == 2 and sum(set(m1)) < d:
#             k+=1
#     print(k)

# import sys
# sys.set_int_max_str_digits(0)
# l = []
# for x in range(1000001):
#     a = 25**340 + 25**79 - 5**60 + x
#     k = 0
#     while a > 0:
#         d = a % 25
#         a = a // 25
#         if d == 0:
#             k += 1
#     if k == 287:
#         l.append(x)
# print(max(l))

# def f(x, A):
#     return (x%3 == 0) <= ((x%5 == 0) <= ((x%3 == 0) and (x%A == 0)))
# m = []
# for A in range(1, 1000):
#     if all([f(x, A) for x in range(1, 1000)]):
#         m.append(A)
# print(max(m))

# import sys
# sys.setrecursionlimit(1000000)
# def f(n):
#     if n < 3:
#         return 1
#     if n > 2:
#         if n%2 == 0:
#             return f(n-1) * (n-1)
#         else: return f(n-2) * (n*2 - 2)
# print((f(10048)-f(10045))//f(10043))

# with open('17.txt') as f:
#     s = [int(x) for x in f]
#     m = []
#     for i in s:
#         if i%36 == 0:
#             m.append(i)
#     b = max(m)
#     k = []
#     for i in range(len(s)-2):
#         c = [h for h in s[i:i+3] if (h > 0 or abs(h) % 100 == 36)]
#         if len(c) >= 2 and sum(s[i:i+3]) <= b:
#             k.append(sum(s[i:i+3]))
#     print(len(k), min(k))