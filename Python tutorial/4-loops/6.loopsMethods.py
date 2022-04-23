### Some loop methods

import re


liste = [1,2,3]

for item in liste:   #elimizde var olan bir listi en bilindik böyle yazdırıyoruz.
    print(item)

"""
Elimizde liste yokken de döngüler ile ekrana bir liste bastırabiliriz (for,while..).
Bunu range() methotu sayesinde yapıyoruz.
"""
#? range()
for item in range(10):  #0'dan 9'a kadar 
    print(item)

for item in range(0,10):  #0'dan 9'a kadar 
    print(item)

for item in range(0,50,5):  #0'dan 50'ye kadar 5'er 5'er
    print(item)

print(list(range(10,20,2))) #list tipine dönüştürüp öyle ekrana bastırtıyoruz

#? enumerate()

greeting = "Hello There"
index = 0
for letter in greeting:
    print(f"letter: {letter}, index: {index}")
    index+=1

for index,letter in enumerate(greeting):
    print(f"index: {index}, letter: {letter}")

for item in enumerate(greeting):
    print(item) # liste tipine dikkat et, Tuple!

#? zip()
list1 = list(range(0,11,2))
list2 = list(range(1,11,2))
list3 = list(zip(list1,list2))
"""
aynı indexte olan değişkenleri eşleyip tuple döndürüyor. 3 liste olsaydı 3'lü tuple,
4 liste olsaydı 4'lü tuple döndürürdü.
"""
print(list3)
