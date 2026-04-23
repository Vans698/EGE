import sys
sys.set_int_max_str_digits(0)
a = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
k = 0
while a > 0:
    d = a % 25
    a = a // 25
    if d == 0:
        k += 1
print(k)

#------------------------------------------------------------

for x in range(2030, 0, -1):
    a = 7**170 + 7**100 - x
    k = 0
    while a > 0:
        d = a % 7
        a = a // 7
        if d == 0: # меняется с условием задачи
            k += 1
    if k == 71:
        print(x)
        break

#------------------------------------------------------------

s = []
for x in range(1, 28001):
    n = 4*28**10 + 3*28**6 + 28**3 - x
    k = 0
    m = n
    while m > 0:
        d = m%28
        m //= 28
        if d == 0:
            k += 1
    s.append([k, n])
s2 = sorted(s)
print(s2[-1][1])

#------------------------------------------------------------
# Большая с/с
def f(x):
  s = []
  while x > 0:
    s.append(x%49)
    x //= 49
  return reversed(s)

d = f(15*2401**1500-10*343**1200+40*49**1000-35*7**850-4805)
r = 0
for i in d:
  if i > 9:
    r += 1
print(r)

#------------------------------------------------------------

c = '0123456789abcdefghijklmnopqrstuvwxyz'[:17]
for x in reversed(c):
    a = f'5432{x}67'
    b = f'302{x}'
    v = int(a, 17) + int(b, 17)
    if v % 19 == 0:
        print(v)

        
c = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')[:17]
for x in reversed(''.join(c)):
    m = f'5432{x}67'
    b = f'302{x}'
    z = int(m, 17) + int(b, 17)
    if z%19 == 0:
        print(z)
#------------------------------------------------------------

c = '0123456789abcdfghijklmnopqrstuvwxyz'[:14]
f = []
for x in c:
  for y in c:
    a = f'14{y}5{x}2'
    b = f'31{x}2{y}3'
    n = int(a, 14) + int(b, 14)
    if n % 9 == 0:
      f.append([int(x, 14) + int(y, 14), int(x, 14), n // 9])
print(max(f)[2])
# c = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
# print(c)