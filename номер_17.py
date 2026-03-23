f = open('17_1.txt')
a = [int(x) for x in f]
k = []
for i in range(len(a)-1):
  if (a[i] %3==0 or a[i+1] %3==0) and ((a[i] + a[i+1])%5==0):
    k.append(a[i] + a[i+1])
print(len(k), max(k))

#------------------------------------------------------------

f = open('17_2.txt')
a = [int(x) for x in f]
k = []
q = []

for h in a:
  if h%2==0:
    q.append(h)
v = sum(q)/len(q)

for i in range(len(a)-1):
  if (a[i] %3==0 or a[i+1] %3==0) and (a[i] < v or a[i+1] < v):
    k.append(a[i] + a[i+1])
print(len(k), max(k))

#------------------------------------------------------------

f = open('DEMO_17.txt')
a = [int(x) for x in f]
k = []
w = []
for c in a:
  if 9 < c < 100:
    w.append(c)
b = min(w)
for i in range(len(a)-1):
  c = (9 < a[i] < 100) + (9 < a[i+1] < 100) # количество двухзначных чисел
  if c == 1 and (a[i]+a[i+1])%b==0: # если двухзачное число только одно
    k.append(a[i] + a[i+1])  
print(len(k), max(k))

#------------------------------------------------------------

f = open('17.txt')
v = [int(x) for x in f]
p = []
m = []

for i in v:
  if 99 < i < 1000 and i%100 == 11:
    m.append(i)


for i in range(len(v)-1):
  c = (99 < v[i] < 1000) + (99 < v[i+1] < 1000)
  if c == 1 and (abs(v[i] - v[i+1])%min(m) == 0):
    p.append(v[i] + v[i+1])
print(len(p), max(p))

#------------------------------------------------------------

f = open('17.txt')
a = [int(x) for x in f]
k = []
w = []
for b in a:
  if b%36==0:
    w.append(b)
n = max(w)
for i in range(len(a)-2):
  c = [h for h in a[i:i+3] if (h > 0 or abs(h) % 100 == 36)]
  # c = (a[i]>0 or abs(a[i])%100==36) + (a[i+1]>0 or abs(a[i+1])%100==36) + (a[i+2]>0 or abs(a[i+2])%100==36) # количество двухзначных чисел
  if len(c) >=2 and sum(a[i:i+3])<=n: # если двухзачное число только одно
    k.append(a[i] + a[i+1] + a[i+2])  
print(len(k), min(k))