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