# Простая последовательность
a = open('24_1.txt')
s = a.readline()
x = 0
v = []
for i in range(len(s)):
  if s[i] == 'X':
    x += 1
    v.append(x)
  else:
    x = 0
print(s, max(v))

#------------------------------------------------------------

a = open('24_8.txt')
s = a.readline()
x = 0
v = []
i = 0
while i < len(s)-1:
  if s[i] in "BCD" and s[i+1] in "AO":
    x += 1
    i += 2
    v.append(x)
  else:
    x = 0
    i += 1
print(max(v))

#------------------------------------------------------------

a = open('24_0.txt')
s = a.readline()
x = 1
v = []
for i in range(len(s)-1):
  if (s[i] == "I" and s[i+1] == "T") or (s[i] == "T" and s[i+1] == 'I'):
    x = 1
  else:
    x += 1
    v.append(x)
print(max(v))

#------------------------------------------------------------

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

#------------------------------------------------------------

a = open('24_0.txt')
s = a.readline()
x = ''
v = []
for i in range(len(s)):
  if s[i] in '1234567890':
    x += s[i]
    v.append(int(x))
  else:
    x = ''
print(max(v))

#------------------------------------------------------------

a = open('24_0.txt')
s = a.readline()
x = ''
v = []
for i in range(len(s)):
  if s[i] in '1234567890ABCDE':
    x += s[i]
    b = (i - len(x))+1
    if int(x, 15)%3 != 0:
      v.append([int(x, 15), x, b])
  else:
    x = ''
print(max(v))

#------------------------------------------------------------

a = open('24_1.txt')
s = a.readline()
x = ''
v = []
for i in range(len(s)):
  if s[i] in x:
    p = x.find(s[i])
    x = x[p + 1:] + s[i]
  else:
    x += s[i]
    v.append(len(x))
print(max(v))

#------------------------------------------------------------

# максимум

a = open('24_2.txt')
s = a.readline()
t = 0
lenn = 0
v = []
for i in range(len(s)):
  if s[i] == 'T':
    t += 1
    lenn += 1
  else:
    lenn += 1
  if t == 100:
    v.append(lenn)
  if t > 100:
    x = s[i-lenn + 1:i+1]
    p = x.find('T')
    x = x[p+1:]
    t = 100
    lenn = len(x)
print(max(v))

#------------------------------------------------------------

with open('24.txt') as f:
  s = f.readline()

m = []
for i in range(len(s)):
  if s[i] == 'A':
    k = 0
    summ = 0
    for x in range(i, len(s)):
      if s[x] in 'AEIUO':
        k += 1
      if s[x] in '0123456789':
        summ += int(s[x])
      if s[x] == 'Z':
        break
    if k == 50 and summ%7 == 0:
      m.append(x-i+1)

print(max(m))

# или
'''
Задача для ровно 100 цифр
1) Максимальную длину
[T]..T...T....T...T...[T]
[A]B..AB....AB........A[B]
b[101] - b[0] + 1 - 2 (берем 102 буквы T и крайние выкидываем)

2) Минимальную длину
T..T...T......T
b[99] - b[0] + 1
'''

# Используем когда ровно одно не менее(условие с двумя буквами ил с одной)
# максимум

a = open('24_2.txt')
s = a.readline()
b = []
for i in range(len(s)):
  if s[i] == 'T':
    b.append(i)

v = []

for i in range(len(b)-101):
  x = b[i+101] - b[i] + 1 - 2
  v.append(x)
print(max(v))

# минимум

a = open('24_3.txt')
s = a.readline()
b = []
for i in range(len(s)):
  if s[i] == 'E':
    b.append(i)

v = []

for i in range(len(b)-239):
  x = b[i+239] - b[i] + 1
  v.append(x)
print(min(v))

# максимум
# два символа

a = open('24.txt')
s = a.readline()
v = []
for i in range(len(s)):
  if s[i] in 'AE' and s[i+1] in 'BCDF':
    v.append(i)

b = []
for i in range(len(v)-131):
  x = v[i+131] + 1 - v[i] +1 -2
  b.append(x)
print(max(b))

# максимум
# когда две буквы и обе строго равны числу
#------------------------------------------------------------

a = open('24.txt')
s = a.readline()
v = []
for i in range(len(s)):
  if s[i] in 'Y':
    v.append(i)

b=[]
for i in range(len(v)-81):
  x = v[i+81] - v[i] + 1 - 2
  if s[v[i]+1:v[i+81]].count('2025') >= 90:
    b.append(x)
print(max(b))

#------------------------------------------------------------

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

#------------------------------------------------------------

a = open('24.txt')
n = a.readline()
s = 0
d = 0
t = 0
l = []
for i in range(len(n)):
  t += 1
  if n[i] == 'S':
    s += 1
  if str(n[i]) in '02468':
    d += 1

  if d == 0:
    s = 0
    t = 0
  if d == 2:
    s = 0
    t = 1
    d = 1

  if d == 1 and s == 35:
    l.append(t)
print(max(l))

#------------------------------------------------------------

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

#------------------------------------------------------------

f = open('224.txt')
a = "_" + f.readline() + "@"

b = []
for i in range(len(a)):
  # i.isdigit(), i.isalpha(), i.islower(), i.isupper()
  if a[i] == '@' or a[i] == '_':
    b.append(i)

m = []
for i in range(1, len(b)-2):
  if a[b[i]] == '@' and a[b[i + 1]] == '_' and b[i+1] - b[i] > 1:
    if a[b[i+1]+1].isalpha() and a[b[i]-1].isalpha():
      x = b[i+2] - b[i-1] + 1 - 2
      y = b[i+2] - b[i] + 1 - 2
      m.append([x, y])
print(max(m)[1])

#------------------------------------------------------------

f = open('24.txt')
a = f.readline()
g = []
for i in range(len(a)):
  if a[i].isdigit():
    if int(a[i])%2 == 0:
      g.append(i)

v = []
for h in range(len(g)-1):
  s = 0
  for j in range(g[h], g[h+1]):
    if a[j] == 'S':
      s += 1
    if s == 35:
      # [g[h]..j]
      v.append(j-g[h]+1)
  # [g[h]..g[h+1])

print(max(v))

#------------------------------------------------------------ 

with open('24.txt') as f:
    s = f.readline()
    v = []
    k = 0
    for i in range(len(s)-4):
        if s[i:i+5] == 'AHAHA':
            v.append(k+4)
            k = 0
        else:
            k += 1
print(max(v))

#------------------------------------------------------------ 

with open('24.txt') as f:
  s = f.read()
  v = []
  for i in range(len(s)-1):
    if s[i] in 'ABC' and s[i+1] in 'ABC':
      v.append(i+1)
  b = []
  for k in range(len(v)-1):
    x = v[k+1] - v[k]
    b.append(x)
print(max(b))