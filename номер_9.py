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
