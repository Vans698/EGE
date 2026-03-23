
#------------------------------------------------------------
#Пробник_ошибки

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

def f(n):
    if n > 10000:
        return 42
    if n <= 10000 and n%2 == 0:
        return 2*n + f(n+3) + f(n+4) + f(n+6)
    if n <= 10000 and n%2 != 0:
        return -(n + f(n+1) + f(n+3))
print(f(9996)-f(9994))

f = open('17_2.2.txt')
a = [int(x) for x in f]
m=[]
for i in a:
    if abs(i)%2026:
        m.append(i)
v = max(m)
l = []
for b in range(len(a)-2):
    c = a[b] + a[b+1]
    if (a[b] < 0 or  a[b+1] < 0) and c <= v:
        l.append(c)
print(len(l), max(l))

def f(s, m):
    if s <= 11: return m%2 == 0
    if m == 0: return 0
    h = [f(s-3, m-1), f(s-7, m-1), f(s//3, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

print([s for s in range(12, 200) if f(s, 2)])
print([s for s in range(12, 200) if f(s, 3) and not(f(s, 1))])
print([s for s in range(12, 200) if f(s, 4) and not(f(s, 2))])



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


