for n in range(1, 10000):
  d = 4*n
  f = bin(d)[2:]
  f += str(f.count('1') % 2)
  f += str(f.count('1') % 2)
  r = int(f, 2)
  if r > 129:
    print(n)
    break

# когда ищем n
  for n in range(1, 10000, 1):
    f = bin(n)[2:]
    if f.count('1') % 2 == 0: 
      f = "10" + f[2:] + '0'
    else: 
      f = "11" + f[2:] + '1'
    r = int(f, 2)
    if r > 40:
      print(n)
      break

# когда ищем min/max r
a = []
for n in range(1, 10000):
  f = bin(n)[2:]
  if f.count('1') % 2 == 0: 
    f += '1'
  else: 
    f += '0'
  if f.count('1') % 2 == 0: 
    f += '1'
  else: 
    f += '0'
  r = int(f, 2)
  if r > 54:
    a.append(r)
print(min(a))

# когда нужно перевести в 3 сс
def three(n):
  s = ""
  while n > 0:
    d = n % 3
    n = n//3
    s = str(d) + s
  return s

a = []
for n in range(1, 10000):
  f = three(n) + str(n%3)
  d = int(f, 3)
  if 99 < d < 1000:
    a.append(d)
print(min(a))