# any - хотя бы одно истинное
# all - все истинны 
# not any - все значения ложные
# not all - хотя бы одно ложное

#------------------------------------------------------------

def f(A, x):
  # (x&A=0)∧¬(x&35≠0→x&52≠0)
  return (x & A ==0) and not((x&35 != 0) <= (x&52 != 0))

for A in range(0, 1000):
  if not any([f(A, x) for x in range(0, 1000)]):
    print(A)
    break # ищем min число(max - range(1000, -1, -1))

#------------------------------------------------------------

def f(A, x, y):
  #(2x−y≥A)∧(y≥17)∧(78≥x)
  return (((2*x)-y>=A) and (y>=17) and (78>=x))

for A in range(1000):
  if not any([f(A, x, y) for x in range(1000) for y in range(1000)]):
    print(A)
    break

#------------------------------------------------------------

def f(A, x):
  return (120%A==0) and ((x%36==0)<=((not(x%A==0))<=(not(x%45==0))))

for A in range(1000, -1, -1):
  if all([f(A, x) for x in range(1, 1000)]):
    print(A)
    break

#------------------------------------------------------------

def f(A, x, y):
  return (2*x-y>=A) and (y>=17) and (78>=x)

for A in range(0, 200):
  if not any([f(A, x, y) for x in range(0, 200) for y in range(0, 200)]):
    print(A)
    break

#------------------------------------------------------------
# для всех способов
def f(x, la, ra):
  return ((5 <= x <= 30) == (14 <= x <= 23)) <= (not(la <= x <= ra))
v = []
for la in range(200):
  for ra in range(la, 200):
    if all([f(x + 0.5, la, ra) for x in range(200)]):
      v.append(ra-la)
print(max(v))
