def f(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  return 2*f(n-1) + f(n-2) # else
print(f(10))

#------------------------------------------------------------

def f(n):
  if n <= 1:
    return 0
  if  n > 1 and n%2 != 0:
    return f(n-1) + 3*n**2
  if n > 1 and n%2 ==0:
    return n//2 + f(n-1) + 2
print(f(49))

#------------------------------------------------------------

import sys
sys.setrecursionlimit(1000000)
def f(n):
  if n < 5:
    return n
  return 2*n * f(n-4) # else
print((f(13766)-9 * f(13762))//f(13758))

#------------------------------------------------------------

import sys
sys.setrecursionlimit(1000000)

def f(n):
  if n >= 7000:
    return n
  return f(n+2)+f(n+3)
print(f(52)-f(56))

#------------------------------------------------------------

import sys
from functools import lru_cache
sys.setrecursionlimit(1000000)

@lru_cache
def f(n):
  if n >= 2025:
    return 1
  return n - f(n+2) - f(n+4)
print(f(20)+f(25))

#------------------------------------------------------------

import sys
sys.setrecursionlimit(100000)
def f(n):
  if n < 3:
    return 1
  if n > 2 and n%2 == 0:
    return f(n-1) * (n-1)
  if n > 2 and n%2 != 0:
    return f(n-2) * (2*n -2)

print((f(10048) - f(10045))//f(10043))

