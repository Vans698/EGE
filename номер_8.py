import itertools

for x in itertools.product("ABC", repeat=2):
    s = "".join(x)
    print(s)

for x in set(itertools.permutations("ABBC", 3)):
    s = "".join(x)
    print(s)


# Найти слово по номеру
import itertools

k = 0
for x in itertools.product("ВЛТУ", repeat=4):
  s = "".join(x)
  k += 1
  if k == 98:
    print(s)

# Найти номер слова с условием
import itertools

k = 0
for x in itertools.product("ДЕКОР", repeat=4):
  s = "".join(x)
  k += 1
  if s[0] == 'К':
    print(k)
    break

# Сколько слов существует с двумя буквами А  
import itertools

k = 0
for x in itertools.product("АБВГ", repeat=4):
  s = "".join(x)
  if s.count("А")==2:
    k += 1
print(k)

import itertools

# на нечетных местах в слове стоит гласная, а на четных согласная
k = 0
for x in itertools.product("АБВГДЕ", repeat=5):
  s = "".join(x)
  if s[0] in "АЕ" and s[1] in "БВГД" and s[2] in "АЕ" and s[3] in "БВГД" and s[4] in "АЕ":
    k += 1
print(k)

# Не может быть идущих подряд одинаковых букв и гласных букв
import itertools

k = 0
for x in itertools.product("СРЕДА", repeat=3):
  s = "".join(x)
  if s[0] != s[1] and s[1] != s[2]:
    if "АЕ" not in s and "ЕА" not in s:
      k += 1
print(k)

# Все буквы различны!!! НЕ должно слово начинаться на Й и не должно быть сочетаний ВФ и ФВ
import itertools

k = 0
for x in set(itertools.permutations("ВАЙФУ", 4)):
    s = "".join(x)
    if s[0] != "Й" and s.count("ВФ") == 0  and s.count("ФВ") == 0:
        k += 1
print(k)

# Первое число не может быть 0 в задачай с числами!!!!
import itertools

k = 0
for x in itertools.product("01234567", repeat=5):
  s = "".join(x)
  if s[0] != "0":
      if s.count("6") == 1 and s.count("16") == 0 and s.count("36") == 0 and s.count("56") == 0 and s.count("76") == 0 and s.count("61") == 0 and s.count("63") == 0 and s.count("65") == 0 and s.count("67") == 0:
        k += 1
print(k)
