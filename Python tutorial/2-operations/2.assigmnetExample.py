import numbers
from unittest import result


x,y,z =2,5,107

numbers = 1,5,7,10,6

#1- kullanıcıdan aldığın bir sayının 2 katı ile x,y,z toplamının farkı nedir
# userNum=float(input("bir sayı giriniz"))*2
# result = userNum-(x+y+z)
# print(result*(-1)) #-'li değer dönerse -1 ile çarpıp mutlağını alabilirsin.

#2- y'nin x'e kalansız bölümünü hesaplayınız 
print(y//x)

#3- (x,y,z) toplamının mod 3'ü nedir
print((x+y+z)%3)

#4- y'nin x. kuvvetini hesaplayınız
print(y**x)

#5- x,*y,z =numbers işlemine göre z'nin küpü kaçtır?
numbers = 1,2,3,4,5,6
x,*y,z = numbers #x 1, z 6, y ise ortada kalan değerleri alır
print(z**3)

#6- x,*y,z =numbers işlemine göre y'nin değerleri toplamı kaçtır
x =0
for a in y:
    x += a
print(f" a eşittir {x}")