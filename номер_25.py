# Тип заданий с диапазоном
# Когда дан диапазон
for x in range(126849, 126872):
  k = []
  for y in range(1, x+1):
    if x%y == 0:
      k.append(y)
  if len(k) == 4:
    print(k)

#------------------------------------------------------------

for x in range(397438, 443521): 
  k = []
  for y in range(2, int(x ** 0.5) + 1):
      if x%y == 0:
          if y % 2 == 0:
              k.append(y)
          y2 = x // y
          if y2 != y and y2 % 2 == 0:
              k.append(y2)
  if len(k) >= 142:
      print(len(k), max(k))

for x in range(397438, 443521):
  k = []
  for y in range(2, int(x**0.5) + 1):
    if x%y == 0:
      if y%2 == 0:
        k.append(y)
      y2 = x//y
      if y != y2 and y2%2 == 0:
        k.append(y2)
  if len(k) >= 142:
    print(len(k), max(k))

#------------------------------------------------------------

# Когда не дан диапазон
# Когда x большое
x = 10 ** 6 + 1
k = 0
while k < 5:
  f = []
  for y in range(1, x+1):
    if x%y == 0:
      if y != 1 and y != x:
        if y % 2 != 0:
          f.append(y)
  if sum(f) > x:
    k += 1
    print(x, sum(f))

  x += 1

#------------------------------------------------------------

# Когда не дан диапазон
# Когда x маленькое
x = 10 ** 6 + 1
k = 0
while k < 5:
  f = []
  for y in range(2, int(x ** 0.5) + 1):
    if x%y == 0:
      if y % 2 != 0:
        f.append(y)
      y2 = x // y
      if y2 != y and y2 % 2 != 0:
        f.append(y2)
  if sum(f) > x:
    k += 1
    print(x, sum(f))

  x += 1

#------------------------------------------------------------

# Можно и так
x = 800000
k = 0
while k < 5:
  x += 1
  f = []
  for y in range(2, int(x ** 0.5) + 1):
    if x%y == 0:
      f.append(y)
      y2 = x // y
      if y2 != y:
        f.append(y2)
  if len(f) > 0 and (min(f) + max(f)) % 10 == 4:
    k += 1
    print(x, min(f) + max(f))

#------------------------------------------------------------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_divisors(x):
    divs = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            if is_prime(i):
                divs.append(i)
            i2 = x // i
            if i2 != i and is_prime(i2):
                divs.append(i2)
    return sorted(divs)  # сортируем для удобства

count = 0
n = 3300001
while count < 5:
    d = prime_divisors(n)
    if len(d) > 0:
        M = d[-1] - d[0]
    else:
        M = 0
    if M % 10 == 5 and str(M) == str(M)[::-1]:
        print(n, M)
        count += 1
    n += 1

#------------------------------------------------------------
'''  если нужно найти ПРОСТЫЕ делители числа
def dell and pr(x):
  a = []
  i = 2
  while i ** 2 <= x:
    if x % i == 0:
      a.append(i)
      while x % i == 0:
        x //= i
    i += 1
  if x > 1:
    a.append(x)
  return a
'''

def pr(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

def dell(x):
    d = []
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            if pr(i):
             d.append(i)
            i_2 = x//i
            if i_2 != i and pr(i_2):
                d.append(i_2) 
    return sorted(d)

x = 3300000
v = []
for n in range(x+1, x+10000):
    a = dell(n)
    if len(a) > 0:
        M = a[-1] - a[0]
    else:
        M = 0
    if M%10 == 5 and str(M) ==str(M)[::-1]:
        print(n, M)

#------------------------------------------------------------

def pr(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

def dell(x):
    d = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            if pr(i):
                d.append(i)
            if i != x//i and pr(x//i):
                d.append(x//i)
    return d

for n in range(7800001, 7850000):
    a = dell(n)
    if len(a) > 0:
        M = max(a) + min(a)
    else:
        M = 0
    if M%100 == 63 and M%len(a) == 0:
        print(n, M)

#------------------------------------------------------------

def dell(x):
  d = []
  for i in range(2, int(x**0.5)+1):
    if x%i == 0:
      if i%2 != 0:
        d.append(i)
      if i != x//i:
        if (x//i)%2 != 0:
          d.append(x//i)
  return sorted(d)


for i in range(321655, 654322, 2):
  d = dell(i)
  if len(d) > 70:
    print(i, d[-1])

#------------------------------------------------------------

# Когда простой делитель
x = 33*10 ** 5 + 1
k = 0
while k < 5:
  x += 1
  f = []
  x2 = x
  for y in range(2, int(x2 ** 0.5) + 1):
    while x2%y == 0:
      f.append(y)
      x2 = x2 // y

  if x2 > 1 and x2 != x:
    f.append(x2)
  if len(f) != 0:
    m = max(f) - min(f)
  else:
    m = 0
  if m % 10 == 5 and str(m) == str(m)[::-1]:
    k += 1
    print(x, m)

#------------------------------------------------------------

def prime(x):
  for i in range(2, int(x**0.5)+1):
    if x%i == 0: 
      return False
  return True

x = 1324727
k = 0
while k < 5:
  x += 1
  for x1 in range(1, int(x**0.5)+1):
    if x % x1 == 0:
      if prime(x1) and prime(x//x1):
        if str(x1).count('5') == 1 and str(x//x1).count('5') == 1:
          print(x, x//x1)
          k += 1

#------------------------------------------------------------

x = 1324727
k = 0
while k < 5:
  x += 1
  dell = []
  for x1 in range(2, int(x**0.5)+1):
    if x % x1 == 0:
      dell.append(x1)
      dell.append(x // x1)
  if len(dell) == 2:
    if str(dell[0]).count('5') == 1 and str(dell[1]).count('5') == 1:
      print(x, dell[1])
      k += 1

#------------------------------------------------------------

# Тип заданий с маской
from fnmatch import fnmatch
for x in range(0, 10**9, 23):
  if fnmatch(str(x), '12345?7?8'):
    f = x//23
    print(x , f)

#------------------------------------------------------------

# Тип заданий с маской
from fnmatch import fnmatch
for x in range(0, int((10**9)**0.5)):
  if fnmatch(str(x**2), '352*6?5*'):
    print(x**2, x)

#------------------------------------------------------------

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


#------------------------------------------------------------

def dell1(x1):
  dell = []
  for x1 in range(1, int(x**0.5)+1):
    if x % x1 == 0:
      dell.append(x1)
      dell.append(x // x1)
  return dell.sort()

k = 0
m = []
for i in range((10**9)-1, (10**8)+1, -1):
   while k <=5:
      a = dell1(i)
      
      
