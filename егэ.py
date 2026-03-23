print("x y w z")
for x in range(2):
  for y in range(2):
    for w in range(2):
      for z in range(2):
        F = ((not(x)) and z and (not(y)) and (not(w))) or ((not(x)) and z and y and (not(w))) or ((not(x)) and z and y and w)
        if F == 1:
          print(x,y,w,z)


for n in range(1, 10000):
    c = bin(n)[2:]
    if n % 5 == 0:
        c += '11'
    else:
        c += str(bin(n//5)[2:])
    r = int(c, 2)
    if r >= 783:
        print(n)
        break

for x in range(1, 7291):
    a = 27**298 + 27**269 - x
    k = 0
    while a > 0:
        d = a % 27
        a = a // 27
        if d == 0:
            k += 1
print(k)

import sys
sys.setrecursionlimit(1000000)
def f(n):
  if n <= 10:
    return n
  return n-12 + f(n-21) # else
print((f(224356)-f(224272))//f(59))

def f(x, y):
  if x == y:
    return 1
  if x > y:
    return 0
  return f(x+1, y) + f(2*x, y) + f(3*x, y)

through_14 = f(6, 14) * f(14, 48)
through_18 = f(6, 18) * f(18, 48)
through_both = f(6, 14) * f(14, 18) * f(18, 48)

result = through_14 + through_18 - through_both
print(result)

#-----егэ-----

# №2
print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((not(x) or y) and z and not(w)) == 1:
                    print(x, y, w, z)

# №5
b = []
for n in range(1, 10000):
    s = bin(n)[2:]
    if n%3 == 0:
        s += s[-3:]
    else:
        s += bin((n%3)*3)[2:]
    r = int(s, 2)
    if r < 130:
      b.append(n)
print(max(b))

# №8
import itertools

k = 0
v = []
for i in itertools.product('ЕИОРТЯ', repeat = 6):
    s = "".join(i)
    k += 1
    if (k%2 == 1) and (s[0] not in 'РТЯ') and (s.count('И') >= 2):
        v.append(k)
print(max(v))

# №14
def night(x):
    s=''
    while x != 0:
        s = str(x%9) + s
        x //= 9
    return s

for x in range(3001):
    v = 9**150 + 9**30 - x
    n = night(v)
    if n.count('0') == 122:
        print(x)
        break

for x in range(3001):
    a = 9**150 + 9**30 - x
    k = 0
    while a > 0:
        d = a % 9
        a = a // 9
        if d == 0: # меняется с условием задачи
            k += 1
    if k == 122:
        print(x)
        break

# №25
def f(A, x, y):
    return (x*y > A) or (x>y) or (11 > x)

for A in range(200, -1, -1):
    if all([f(A, x, y) for x in range(0, 200) for y in range(0, 200)]):
        print(A)
        break

# №16
import sys
sys.setrecursionlimit(10000)
def f(n):
    if n < 10:
        return n
    return 3*n + f(n-3)
print(((f(6250)+2)*(6244))//f(6238))

# №17
f  = open('17_23201.txt')
a = [int(x) for x in f]
v = []
k = []
for c in a:
    if (99 < c < 1000) and c%10 == 7:
        v.append(c)
b = min(v)  
for i in range(1, len(a)-1):
    c = (99 < a[i] < 1000) + (99 < a[i+1] < 1000)
    if c == 1 and (a[i] + a[i+1])%b==0:
        k.append(a[i] + a[i+1])
print(len(k), min(k))

# 19 20 21
def f(s, m):
    if s <= 35: return m%2 == 0
    if m == 0: return 0
    c = [f(s-i, m-1) for i in range(2, 5, 2)] + [f((s+1)//2, m-1)]
    return any(c) if (m-1) % 2 == 0 else all(c) # any(c) когда при неудачном ходе первого
print([s for s in range(36, 200) if f(s, 2)])
print([s for s in range(36, 200) if f(s, 3) and not(f(s, 1))])
print([s for s in range(36, 200) if f(s, 4) and not(f(s, 2))])

from turtle import *
tracer(0)
screensize(3000, 3000)
c = 25
lt(90)
for i in range(2):
    fd(3*c)
    rt(90)
    fd(20*c)
    rt(90)
up()
bk(8*c)
rt(90)
fd(9*c)
lt(90)
down()
for i in range(2):
    fd(16*c)
    rt(90)
    fd(8*c)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*c, y*c)
        dot(3, 'blue')
update()
exitonclick()

def f(x, y):
    if x == y:
        return 1
    if x < y or x == 13:
        return 0
    return f(x-1, y) + f(x-2, y) + f(x//3, y)

print(f(19, 6)*f(6, 4))


def f(x, y):
  if x == y:
    return 1
  if x > y:
    return 0
  return f(x+1, y) + f(x+2, y) + f(x+3, y)

def g(x, y):
    if x != y:
        return f(x, y)
    return 0

print(g(0, 5))

def three(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x = x//3
    return s

v = []
for n in range(1, 100000):
    n2 = sorted(three(n), reverse=True)
    n2 = ''.join(n2) + max(n2)
    r = int(n2, 3)
    if r < 1200:
        v.append(r)
print(max(v))


from turtle import *
tracer(0)
screensize(10000, 10000)
c = 8
lt(90)

up()
fd(10*c)
down()
for i in range(6):
    fd(50*c)
    rt(90)
    fd(43*c)
    rt(90)
up()
fd(40*c)
rt(90)
fd(40*c)
down()
for i in range(9):
    fd(40*c)
    lt(90)
    fd(20*c)
    lt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*c, y*c)
        if x == 0 or y == 0:
            dot(3, 'red')
        else:
            dot(3, 'blue')
update()
exitonclick()

from itertools import product

k=0
for x in product('0123456789ABCD', repeat=5):

    if x[0] == '0':
        continue

    v = True
    for i in range(5):
        if x[i] in 'ABCD':
            if i > 0 and x[i-1] in '13579':
                v = False
                break
            if i < 4 and x[i+1] in '13579':
                v = False
                break

    if v:
        k += 1

print(k)


c = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')[:17]
for x in reversed(''.join(c)):
    m = f'5432{x}67'
    b = f'302{x}'
    z = int(m, 17) + int(b, 17)
    if z%19 == 0:
        print(z)

import sys
sys.setrecursionlimit(1000000000)

def f(n):
    if n <= 1000:
        return n**(n**2)
    if n > 1000:
        return n + (2*f(n-2)) + (6*f(n-6))

print(f(20024) - (2*f(20022)) - (3*f(20020)) + (18*f(20014)))


def f(s, m):
    if s >= 342: return m%2 == 0
    if m == 0: return 0
    c = [f(s+7, m-1), f(s*3, m-1)]
    return any(c) if (m-1) % 2 == 0 else all(c)

print([s for s in range(1, 301) if f(s, 2)])
print([s for s in range(1, 301)if f(s, 3) and not(f(s, 1))])
print([s for s in range(1, 301)if f(s, 4) and not(f(s, 2))])


def f(x, y):
    if x == y:
        return 1
    if x < y or x == 12:
        return 0
    return f(x-3, y) + f(x//2, y)
print(f(80, 23)*f(23, 3))

a = open('24.txt')
s = a.readline()
g = []
k = 0
for i in range(len(s)):
    if s[i] == 'E':
        k += 1
        for x in range(i+1, len(s)):
            if s[x] in 'ND':
                k += 1
            elif s[x] == 'E':
                g.append(k+1)
                k = 0
                break
            else:
                k = 0
                break
print(max(g))   

# 17
s = open('17.txt')
a = [int(x) for x in s]

v = []
for i in a:
    if 1000 <= abs(i) <= 9999:
        v.append(i)
v_m = max(v)

l = []
for i in range(len(a)-1):
    if abs(a[i]-a[i+1]) >= v_m:
        l.append(a[i]+a[i+1])
print(len(l), max(l))

#------------------------------------------------------------
#Пробник_ошибки

f = open('9.txt')
c = 0
for k in f:
    m = [int(x) for x in k.split()]
    m1 = []
    m2 = []
    for i in m:
        if m.count(i) == 1:
            m1.append(i)
        if m.count(i) == 2:
            m2.append(i)
    if len(m1) == 3 and len(m2) == 4 and sum(m1)/len(m1) > sum(m2)/len(m2):
        c += 1
print(c)

print(bin(168)[2:])
print(bin(160)[2:])

def f(n):
    if n > 10000:
        return 42
    if n <= 10000 and n%2 == 0:
        return 2*n + f(n+3) + f(n+4) + f(n+6)
    if n <= 10000 and n%2 != 0:
        return -(n + f(n+1) + f(n+3))
print(f(9996)-f(9994))

f = open('17_2.2.txt')
a = [int(x) for x in f]
m=[]
for i in a:
    if abs(i)%2026:
        m.append(i)
v = max(m)
l = []
for b in range(len(a)-2):
    c = a[b] + a[b+1]
    if (a[b] < 0 or  a[b+1] < 0) and c <= v:
        l.append(c)
print(len(l), max(l))

def f(s, m):
    if s <= 11: return m%2 == 0
    if m == 0: return 0
    h = [f(s-3, m-1), f(s-7, m-1), f(s//3, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

print([s for s in range(12, 200) if f(s, 2)])
print([s for s in range(12, 200) if f(s, 3) and not(f(s, 1))])
print([s for s in range(12, 200) if f(s, 4) and not(f(s, 2))])



f = open('24var02.txt')
a = f.readline()
x = []
for i in range(len(a)-2):
    if a[i:i+3] == 'CAT':
        x.append(i)

al = 0
for i in x:
    one = 0
    cat = 0
    for f in range(i, -1, -1):
        if a[f] == '1':
            one += 1
        if f <= len(a)-3 and a[f:f+3] == 'CAT':
            cat += 1
        if one == 700 and cat >= 4:
            lenn = i+2 - f + 1
            if lenn > al:
                al = lenn
            break  
        if one > 700:
            break
        
print(al)


