### Iterators
"""
iterable = yinelenebilir
iterator = yineleyici

Aşşağıdaki list, bir iterable objedir.
"""


liste = [1,2,3,4,5,6,7,8,9]
# print(dir(liste))   #iter methotuna sahiptir. Şöyle diyebiliriz: iter methoduna sahip olan veriler/tipler iterabledır.

iterator = iter(liste)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(iterator)
print(liste)