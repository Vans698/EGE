# Честная игра
# 19 задание делает в ручную, если нечестная игра (x + s*y >= z)
# s1 - количество камней в первой куче
# s2 - количество камней во второй куче
# n  - оставшееся количество ходов
# Функция возвращает True/False в зависимости от того, выигрышная позиция или нет


def f(s1, s2, n):
  if s1 + s2 >= 59:
    return False
  if n == 0:
    return True
  a = [f(s1 + 1, s2, n - 1), f(s1 * 2, s2, n - 1), f(s1, s2 + 1, n - 1), f(s1, s2 * 2, n - 1)]
  # return False in a - альтернативная проверка №1
  # return not all(a) - альтернативная проверка №2
  if False in a:
    return True
  else:
    return False

# 20 задание
for s in range(1, 54):
  if f(5, s, 3) and not f(5, s, 1):
    print(s)

# 21 задание
for s in range(1, 54):
  if not f(5, s, 4) and f(5, s, 2):
    print(s)

#------------------------------------------------------------

def main(s1, s2, n):
  if s1 + s2 >= 65:
    return False
  if n == 0:
    return True
  a = [main(s1+1, s2, n-1), main(s1*3, s2, n-1), main(s1, s2+1, n-1), main(s1, s2*3, n-1)]
  return False in a

for s2 in range(1, 58+1):
  if not main(6, s2, 1) and main(6, s2, 3):
    print(s2)

for s2 in range(1, 58+1):
  if not main(6, s2, 4) and main(6, s2, 2):
    print(s2)

#------------------------------------------------------------

def f(s, m):
    if s <= 35: return m%2 == 0
    if m == 0: return 0
    c = [f(s-i, m-1) for i in range(2, 5, 2)] + [f((s+1)//2, m-1)]
    return any(c) if (m-1) % 2 == 0 else all(c) # any(c) когда при неудачном ходе первого
print([s for s in range(36, 200) if f(s, 2)])
print([s for s in range(36, 200) if f(s, 3) and not(f(s, 1))])
print([s for s in range(36, 200) if f(s, 4) and not(f(s, 2))])

#------------------------------------------------------------d

def f(s1, s2, m):
    if s1+s2 >= 65: return m%2 == 0
    if m == 0: return 0
    c = [f(s1+1, s2, m-1), f(s1, s2+1, m-1), f(s1*3, s2, m-1), f(s1, s2*3, m-1)]
    return any(c) if (m-1) % 2 == 0 else all(c) # any(c) когда при неудачном ходе первого
# print([s2 for s2 in range(1, 59) if f(6, s2, 2)])
print([s2 for s2 in range(1, 59) if f(6, s2, 3) and not(f(6, s2, 1))])
print([s2 for s2 in range(1, 59) if f(6, s2, 4) and not(f(6, s2, 2))])

#------------------------------------------------------------

def f(s1, s2, m):
    if s1 == s2: return m%2 == 0
    if m == 0: return 0
    if s1<s2:
        c = [f(s1+1, s2, m-1), f(s1+2, s2, m-1)]
    else:
        c = [f(s1, s2+1, m-1), f(s1, s2+2, m-1)]
    return any(c) if (m-1)%2 == 0 else all(c)
print([s2 for s2 in range(1, 15) if f(15, s2, 2)], end='')
print([s2 for s2 in range(16, 31) if f(15, s2, 2)])

print([s2 for s2 in range(1, 15) if f(15, s2, 3) and not(f(15, s2, 1))], end=' ')
print([s2 for s2 in range(16, 31) if f(15, s2, 3) and not(f(15, s2, 1))])

print([s2 for s2 in range(1, 15) if f(15, s2, 4) and not(f(15, s2, 2))], end=' ')
print([s2 for s2 in range(16, 31) if f(15, s2, 4) and not(f(15, s2, 2))])

#------------------------------------------------------------

def f(s1, s2, m, x):
    if s1 + s2 <= 42: return m%2 == 0
    if m == 0: return 0
    if x == '1-4':
        c = [f(s1, s2-4, m-1, '2-4'), f(s1//3, s2, m-1, '1//3'), f(s1, s2//3, m-1, '2//3')]
    elif x == '2-4':
        c = [f(s1-4, s2, m-1, 'x-4'), f(s1//3, s2, m - 1, '1//3'), f(s1, s2 // 3, m - 1, '2//3')]
    elif x == '1//3':
        c = [f(s1-4, s2, m-1, '1-4'), f(s1, s2-4, m-1, '2-4'), f(s1, s2//3, m-1, '2//3')]
    elif x == '2//3':
        c = [f(s1-4, s2, m-1, '1-4'), f(s1, s2-4, m - 1, '2-4'), f(s1//3, s2, m - 1, '1//3')]
    else:
        c = [f(s1-4, s2, m-1, '1-4'), f(s1, s2 - 4, m - 1, '2-4'), f(s1 // 3, s2, m - 1, '1//3'), f(s1, s2//3, m - 1, '2//3')]
    return any(c) if (m-1)%2 == 0 else all(c)

print([s2 for s2 in range(1, 150) if f(50, s2, 2, '')])
print([s2 for s2 in range(1, 150) if f(50, s2, 3, '') and not(f(50, s2, 1, ''))])
print([s2 for s2 in range(1, 150) if f(50, s2, 4, '') and not(f(50, s2, 2, ''))])
