print("x y w z")
for x in range(2):
  for y in range(2):
    for w in range(2):
      for z in range(2):
        F = (x and not(y)) or (y == z) or not(w)
        if F == 0: # если все F нули
          print(x,y,w,z)
