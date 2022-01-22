###Tuple
# Tuple tanımlarken parantez kullanmana gerek yoktur fakat kullanırsan daha okunabilir bir kod yazmış olursun.
from cmath import pi


tuple = (1,"iki",3)
list = [1,"iki",3]
print(tuple)


print(type(tuple))
print(type(list))


print(tuple[2])
print(list[2])

print(len(tuple))
print(len(list))

list = ["asd","asda"]
tuple = ("asdd","asdda")  #burada tuple adındaki değişkene en baştan bir değer atadık dikkat et

print(list)
print(tuple)   

list[0] = "ahmet"
#tuple[0] = "ali"    # list ile tuple arasındaki en önemli fark burada ortaya çıkıyor.

#! Tuple içerisindeki değerler değiştirilemez. Silme, güncelleme, ekleme yapılamaz

print(tuple.count("ayşe"))
print(tuple.index("asdda"))

tuple1 = (1,2,3)
tuple2 = (4,5,6)
tupleTotal = tuple1+tuple2
print(tupleTotal)