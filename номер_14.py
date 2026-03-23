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