# нет дополнительных условий
# x -> y
def f(x, y):
  if x == y:
    return 1
  if x > y:
    return 0
  return f(x+1, y) + f(4*x, y)

print(f(3, 44))

#------------------------------------------------------------

# траектория вычислений содержит точку 18
# x -> y
def f(x, y):
  if x == y:
    return 1
  if x > y:
    return 0
  return f(x+1, y) + f(2*x, y)

print(f(3, 18)*f(18, 37))

#------------------------------------------------------------

#траектория вычислений не содержит точки 6 и 12
# x -> y
def f(x, y):
  if x == y:
    return 1
  if x > y or x == 6 or x == 12:
    return 0
  return f(x+1, y) + f(2*x, y) + f(x+3, y)

print(f(3, 16))

#------------------------------------------------------------

#траектория вычислений содержит точку 13 и не содержит точку 9
# x -> y
def f(x, y):
  if x == y:
    return 1
  if x > y or x == 29:
    return 0
  return f(x+1, y) + f(2*x, y) + f(3*x, y)

print(f(2, 13) * f(13, 44))

#------------------------------------------------------------

def f(x, y):
  if x == y:
    return 1
  if x < y or x == 25:
    return 0
  return f(x-3, y) + f(x-4, y) + f(x//3, y)
print(f(47, 15) * f(15, 6))

#------------------------------------------------------------
# Особые задачи
#------------------------------------------------------------

def w(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return w(x+1, y) + w(2*x, y)
print(((w(1, 10) * w(10, 40)) + (w(1, 15) * w(15, 40))) - (w(1, 10) * w(10, 15) * w(15, 40)))

#------------------------------------------------------------

def f(x, y, z=None):
    if x == y: return 1
    if x > y: return 0
    total = 0
    if z != 'x+1': total += f(x+1, y, 'x+1')
    if z != 'x+2': total += f(x+2, y, 'x+2')
    if z != 'x+4': total += f(x+4, y, 'x+4')
    if z != 'x+8': total += f(x+8, y, 'x+8')
    return total

print(f(16, 48))

#------------------------------------------------------------

def Sum(x):
    s = 0
    while x > 0:
        s += x%10
        x //= 10
    return s

def f(x, y):
    if x == y: return 1
    if x < y: return 0
    return f(x - int(str(x**2)[0]), y) + f(x - Sum(x), y)
print(f(32, 1))