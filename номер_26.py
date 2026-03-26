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