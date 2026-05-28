# Выбор под последовательности
f = open('26.txt')
a = [int(x) for x in f]
a.pop(0)
a.sort(reverse=True)
k = 0
for i in range(len(a)):
  if i%6 == 5:
    k += a[i]//2
  else:
    k += a[i]
print(k)

#------------------------------------------------------------

# Жадный алгоритм
f = open('26.txt')
a = [int(x) for x in f]
s = 8200
a.sort(reverse=False)
k = 0
p = 0
w = []
for i in range(len(a)):
  if k+a[i] <= s:
    k += a[i]
    p += 1
  if a[i]>29 and a[i] <= 53:
    w.append(a[i])
print(p, a[p - 1], k, max(w))


#
f = open('26var02.txt')
a = [int(x) for x in f]
N = 815
M = 717
b = sorted(a[:815], reverse=True) # команды
c = sorted(a[815:], reverse=True) # самолеты
k = 0
l = 0
for i in b:
  t = c[0]
  if t >= i:
    k += 1
    if i > l:
      l = i
    c = c[1:]
print(k, l)

#------------------------------------------------------------

# Сортировка по нескольким столбцам
f = open('26.txt')
s = 6000
a = [[int(y) for y in x.split()] for x in f]
a.sort()
r = []
m=1
for i in range(len(a)-1):
  if a[i][0] == a[i+1][0] and a[i+1][1] - a[i][1] == 1:
    m +=1
    r.append([a[i][0], m])
  else:
    m = 1
print(max(r, key=lambda x: (x[1], x[0])))


#
f = open('26.txt')
a = [[int(y) for y in x.split()] for x in f]
N = 8765
P = [40, 40, 39, 44]
b = []
v = []

for i in a:
  h = 0
  for k in range(4):
    if i[k+1] >= P[k]:
      h += 1
      
  if h == 4:
    b.append([i[0], sum(i[1:5])])
  if h == 0:
    v.append([i[0], sum(i[1:5])])


b2 = sorted(b, key = lambda x: (-x[1], x[0]))
v2 = sorted(v, key = lambda x: (-x[1], x[0]))

print(b2[-1], v2[0])

#------------------------------------------------------------

f = open('26.txt')
a = [x for x in f]
r = 199154
cn = 95324
minn = [int(x) for x in a[:r]]
m_and_p = [[int(x) for x in y.split()] for y in a[r:]]

minn = sorted(minn)
m_and_p = sorted(m_and_p)

mp = [0] * cn
mp[-1] = cn - 1
for i in range(cn - 2, -1, -1):
  if m_and_p[i][1] < m_and_p[mp[i + 1]][1]:
    mp[i] = i
  else:
    mp[i] = mp[i + 1]

j = 0
p = 0
b = []
for i in minn:
  while i > m_and_p[j][0]:
    j += 1
  p += m_and_p[mp[j]][1]
  b.append(m_and_p[mp[j]][0])
print(p, max(b))

#------------------------------------------------------------

f = open('26.txt')
a = [[int(y) for y in x.split()] for x in f]
a.sort(key = lambda x: (x[0] + x[1], x[0]))

al = []
v = [a[0]]
for i in range(len(a)):
    if (v[-1][0] + v[-1][1]) <= (a[i][0]):
        v.append(a[i])

for i in range(len(a)):
    if (v[-2][0] + v[-2][1]) <= (a[i][0]):
        v[-1] = a[i]
print(len(v), 20_000 - (v[-1][0] + v[-1][1]))

#------------------------------------------------------------

with open('26.txt') as f:
  a = [[int(y) for y in x.split()] for x in f]
  room = 18
  query = 5187
  a.sort()
  rooms = [-1] * room
  true = 0
  for q in range(len(a)):
    for r in range(len(rooms)):
      if a[q][0] > rooms[r]:
        rooms[r] = a[q][1]
        true += 1
        break
print(true, rooms)