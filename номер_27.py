# Часть 1
f = open('27_A.txt')
cluster1 = []
cluster2 = []
for i in f:
    cluster = [float(x.replace(',', '.')) for x in i.split()]
    if cluster[1] < 8:
        cluster1.append(cluster)
    else:
        cluster2.append(cluster)

def dist(x1, y1, x2, y2):
  return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def calculate(cluster):
    sums = []
    for p in range(len(cluster)):
        x = cluster[p][0]
        y = cluster[p][1]
        v = sum(dist(x, y, cluster[i][0], cluster[i][1]) for i in range(len(cluster)))
        sums.append([v, x, y])
    return min(sums)

s1 = calculate(cluster1)
s2 = calculate(cluster2)

print(s1, s2)

# Часть 2
f = open('27_B.txt')
cluster1 = []
cluster2 = []
cluster3 = []
for i in f:
    cluster = [float(x.replace(',', '.')) for x in i.split()]
    if cluster[1] < 20:
        cluster1.append(cluster)
    elif cluster[0] > 18:
        cluster2.append(cluster)
    else:
        cluster3.append(cluster)

def dist(x1, y1, x2, y2):
  return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def calculate(cluster):
    sums = []
    for p in range(len(cluster)):
        x = cluster[p][0]
        y = cluster[p][1]
        v = sum(dist(x, y, cluster[i][0], cluster[i][1]) for i in range(len(cluster)))
        sums.append([v, x, y])
    return min(sums)

def calculate_2(x, y, cluster):
    v = max(dist(x, y, cluster[i][0], cluster[i][1]) for i in range(len(cluster)))
    return v

s1 = calculate(cluster1)
s2 = calculate(cluster2)
s3 = calculate(cluster3)

a1 = calculate_2(s1[1], s1[2], cluster1)
a2 = calculate_2(s2[1], s2[2], cluster2)
a3 = calculate_2(s3[1], s3[2], cluster3)

print(len(cluster1), s1)
print(len(cluster2), s2)
print(len(cluster3), s3)

print('B1:', dist(s1[1], s1[2], s2[1], s2[2])*10000)
print('B2:', max(a1, a2, a3)*10000)