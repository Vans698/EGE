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