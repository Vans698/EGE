a = 7*49**120 - 6*343**65 - 5*7**40
k = 0
while a > 0:
    d = a % 7
    a = a//7
    if d == 6:
        k += 1
print(k)

print("x y w z")
for x in range(2):
  for y in range(2):
    for w in range(2):
      for z in range(2):
        F = (not(z) and not(x==y)) <= (not(y or w))
        if F == 0:
          print(x,y,w,z)

print("a b c d")
for a in range(2):
  for b in range(2):
    for c in range(2):
      for d in range(2):
        F = c and (a or d) and (d <= b)
        if F == 0:
          print(a,b,c,d)
print("Ответ: bcad") 

print("x y w z")
for x in range(2):
  for y in range(2):
    for w in range(2):
      for z in range(2):
        F = (((w==1)<=z)and((not(y)) and x))
        if F == 1:
          print(x,y,w,z)

def cf(n):
  s =''
  while n > 0:
    d = n%3
    n = n//3
    s = str(d) + s
  return s
  
a = []
for n in range(1, 10000):
  g = cf(n)
  if n % 3 == 0:
    g = '1' + g + '02'
  else:
    f = cf((n%3)*4)
    g = g + f
  r = int(g, 3)
  if r < 100:
    a.append(n)
print(max(a))

# -----------ДЗ-----------
def f(x, y):
    if x == y:
        return 1
    if x > y or x == 10:
        return 0
    return f(x+1, y) + f(x+2, y) + f(x*2, y)
print(f(3, 7) * f(7, 20))

def f(x, y):
    if x == y:
        return 1
    if x < y or x == 25:
        return 0
    return f(x-3, y) + f(x-4, y) + f(x//3, y)
print(f(47, 15) * f(15, 6))

def F(n):
    if n <= 1:
        return 1
    if n >1 and n%3 == 0:
        return F(n-1) + F(n-3)
    return F(n-2)+3*n
print(F(65))

import sys
sys.setrecursionlimit(1000000)

def F(n):
    if n <= 5:
        return 1
    return n + F(n-2)
print(F(2126)-F(2122))

# -----------ДЗ-----------
import itertools

k = 0
for x in itertools.product('ДРАКОН', repeat=8):
    s = ''.join(x)
    if s.count('А') == 1 and s.count('О') == 1:
        k += 1
print(k)

import itertools

k = 0
for x in itertools.product('ЭТАН', repeat=5):
    s = ''.join(x)
    if (s.count('Э') == 1 and s.count('А') == 0) or (s.count('Э') == 0 and s.count('А') == 1):
        k += 1
print(k)

# -----------ДЗ-----------
from fnmatch import fnmatch
for x in range(0, 10**10, 96437):
  if fnmatch(str(x), '7?2*4??9?'):
    f = x//96437
    print(x , f)

for x in range(397438, 443520):
    k = []
    for y in range(1, x+1):
        if x%y == 0:
            k.append(y)
    if len(k) == 142:
        print(k)

# -----------ДЗ-----------
def f(A, x, y):
    return  (2*x+y !=110)or(x<y)or(A<x)

for A in range(200, -1, -1):
    if all([f(A, x, y) for x in range(1000) for y in range(1000)]):
        print(A)
        break

def h(A, x):
    return (((x&52)!=0) and ((x&48)==0)) <= (not((x&A)==0))

for A in range(1000):
    if all([h(A, x) for x in range(1000)]):
        print(A)
        break

def g(A, x):
    return ((x%100!=0) and (x%4==0)) or (x%400==0) or (x%A!=0)

for A in range(1, 1000):
    if all([g(A, x) for x in range(1, 1000)]):
        print(A)
        break

# -----------ДЗ-----------
f = open('17_1.txt')
a = [int(x) for x in f]
k = []
w = []
for c in a:
  if 999 < c < 10000:
    w.append(c)
r = max(w)
for i in range(len(a)-1):
    g = abs(a[i]-a[i+1])
    if g >= r:
        k.append(a[i] + a[i+1])
print(len(k), max(k))

f = open('17_2.txt')
a = [int(x) for x in f]
k = []
v = []
for b in a:
  if b%2025 == 0:
    v.append(b)
n = min(v)
for i in range(len(a)-2):
  c = [h for h in a[i:i+3] if (h%n)==0]
  if len(c) >= 1 and (99999 < (a[i]+a[i+1]+a[i+2]) < 1000000):
    k.append(a[i]+a[i+1]+a[i+2])
print(len(k), max(k))

# -----------ДЗ-----------
def e(x, y):
    if x == y:
        return 1
    if x > y or x == 15:
        return 0
    return e(x+1, y) + e(2*x, y)
c = e(1, 10)*e(10, 40)

def w(x, y):
    if x == y:
        return 1
    if x > y or x == 10:
        return 0
    return w(x+1, y) + w(2*x, y)
print((w(1, 15)*w(15, 40)) + c )

#--------

def w(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return w(x+1, y) + w(2*x, y)
print(((w(1, 10) * w(10, 40)) + (w(1, 15) * w(15, 40))) - (w(1, 10) * w(10, 15) * w(15, 40)))

# --------

def main(s1, s2, n):
    if s1 + s2 >= 231:
        return False
    if n == 0:
        return True
    a = [main(s1 + 4, s2, n - 1), main(s1*3, s2, n - 1), main(s1, s2 + 4, n - 1), main(s1, s2*3, n - 1)]
    if False in a:
        return True
    else:
        return False
    
for s2 in range(1, 217+1):
    if not main(10, s2, 1) and main(10, s2, 3):
        print(s2)

for s2 in range(1, 217+1):
    if main(10, s2, 4) and not main(10, s2, 2):
        print(s2)

# -----------ДЗ-----------

a = open('24_9.txt')
s = a.readline()
x = 0
v = []
i = 0
while i < len(s) - 3:
    if (s[i] == 'N' and s[i+1] == 'P' and s[i+2] == 'O') or (s[i] == 'P' and s[i+1] == 'N' and s[i+2] == 'O'):
        x += 1
        i += 3
        v.append(x)
    else:
        i += 1
        x = 0
print(max(v))

a = open('24.txt')
s = a.readline()
x = 1
v = []
for i in range(len(s)-1):
    if (s[i] == 'X' and s[i+1] == 'X') or (s[i] == 'Y' and s[i+1] == 'Y'):
        x = 1
    else:
        x += 1
        v.append(x)
print(max(v))

# -----------ДЗ-----------

def f(s1, s2, m):
    if s1 + s2 <= 42: return m%2 == 0
    if m == 0: return 0
    if s1 >= 4 and s2 >= 4: h = [f(s1-4, s2, m-1), f(s1, s2-4, m-1), f(s1//3, s2, m-1), f(s1, s2//3, m-1)]
    elif s1 < 4 and s2 >= 4: h = [f(s1, s2-4, m-1), f(s1//3, s2, m-1), f(s1, s2//3, m-1)]
    elif s1 >= 4 and s2 < 4: h = [f(s1-4, s2, m-1), f(s1//3, s2, m-1), f(s1, s2//3, m-1)]
    else: h = [f(s1//3, s2, m-1), f(s1, s2//3, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h) # any(c) когда при неудачном ходе первого

print([s2 for s2 in range(2, 200) if f(50, s2, 2)])
print([s2 for s2 in range(2, 200) if f(50, s2, 3) and not(f(50, s2, 1))])
print([s2 for s2 in range(2, 200) if f(50, s2, 4) and not(f(50, s2, 2))])


def f(s, m):
    if s <= 11: return m%2 == 0
    if m == 0: return 0
    c = [f(s-3, m-1), f(s-7, m-1), f(s//3, m-1)]
    return any(c) if (m-1)%2 == 0 else all(c)

print([s for s in range(12, 100) if f(s, 2)])
print([s for s in range(12, 100) if f(s, 3) and not(f(s, 1))])
print([s for s in range(12, 100) if f(s, 4) and not(f(s, 2))])

# -----------ДЗ-----------

from turtle import *
tracer(0)
screensize(3000,3000)
c=25
lt(90)
rt(30)
for i in range(10):
    fd(30*c)
    rt(60)
    fd(30*c)
    rt(120)
up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*c,y*c)
        if x == 0 or y == 0:
            dot(3, 'red')
        else:
            dot(3,'blue')

goto(-100 * c, 100 * c)
fd(200 * c)



update()
exitonclick()

from turtle import *
tracer(0)
screensize(3000,3000)
c=25
lt(90)
rt(90)
for i in range(12):
    fd(9*c)
    rt(72)
up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*c,y*c)
        if x == 0 or y == 0:
            dot(3, 'red')
        else:
            dot(3,'blue')

goto(-100 * c, 100 * c)
fd(200 * c)

update()
exitonclick()

def prime(x):
  for v in range(2, int(x**0.5) + 1):
    if x % v == 0:
      return False
  return True


from fnmatch import fnmatch

n = []
for x in range(1, 10**11):
  if fnmatch(str(x), '*2025*') and (x % 10) > 1:
    n.append(x)
b = sorted(n, reverse = True)

if len(b) >= 3:
    y = b[2]
    dell = []
    for c in range(1, int(y**0.5) + 1):
        if y % c == 0:
            dell.append(c)
            if c != y//c:
                dell.append(y//c)
    f = len(dell)


    if prime(f):
        if f%2 != 0:
            dell.remove(y)
            print(max(dell))


