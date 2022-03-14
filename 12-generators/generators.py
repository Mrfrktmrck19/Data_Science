### Generators
"""
Generator, bellekte yer işgal etmeyen bir iterator üretiyor.
"""

# def cube():
#     result = []
#     for i in range(5):
#         result.append(i**3)
#     return result    

# print(cube())

"""
Yukarıdaki fonksiyonun amacı sadece ekrana bir liste bastırmaktır. 5 Adet değer basacağı için bellekte
yer kaplaması göz ardı edilebilir ama daha fazla olursa sorun çıkar. Zaten amacı sadece ekrana bir şey
basmak olduğu için bellekte yer kaplamasına da gerek yok. Bunun yerine yield keywordunu kullanabiliriz.
"""

def cube():
    for i in range(5):
        yield i**5

generator = cube()
print(generator)  #iterable obje üretiyor (tabi generator), üzerinde dolaşmak için next methodunu kullan


iterator = iter(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))