f = open('9.txt')
c=0
for i in f:
    m = [int(x) for x in i.split()]
    m2 = []
    m1 = []
    for j in m:
        if m.count(j) == 2:
            m2.append(j)
        if m.count(j) == 1:
            m1.append(j)
    if len(m2) == 6 and len(m1) == 1:
        if (min(m2) + max(m2))/2 < m1[0]:
            c += 1
print(c)

# ------------------------------------------------------------

f = open('9.txt')
c = 0
for k in f:
    m = [int(x) for x in k.split()]
    m1 = []
    m2 = []
    for i in m:
        if m.count(i) == 1:
            m1.append(i)
        if m.count(i) == 2:
            m2.append(i)
    if len(m1) == 3 and len(m2) == 4 and sum(m1)/len(m1) > sum(m2)/len(m2):
        c += 1
print(c)

# ------------------------------------------------------------

import math

f = open('26.txt')
c = 0
for i in f:
  m = [int(x) for x in i.split()]
  m1 = []
  m2 = []
  for j in m:
    if j%2 == 0:
      m1.append(j)
    if j%2 != 0:
      m2.append(j)
  if len(m1)>=2 and len(m2)>=2:
    if (sum(m2))*3 > math.prod(m1):
      c += 1
print(c)

# ------------------------------------------------------------

f = open('9.txt')
c = 0
for i in f:
    c += 1
    a = [int(x) for x in i.split()]
    m1 = []
    m2 = []
    for j in a:
        if a.count(j) == 1:
            m1.append(j)
        if a.count(j) == 3:
            m2.append(j)
    if len(m1) == 4 and len(m2) == 3 and max(a) in m2 and (max(a)) % 10 == 0:
        print(c)
        break 