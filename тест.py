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