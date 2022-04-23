### Identity (is) & Membership (in) Operators

# Identity Operator: is
x = y = [1,2,3] #x ile y aynı adresi gösterirler, pythonda bir liste başka bir list atadığında referansla atıyordu hatırla!
z = [1,2,3]
print(x==y) #burada  x ile y'nin değerlerine(value) bakınır,
print(x==z) #yukarıdaki karşılaştırma ile aynı

print(x is z) # burada hem değerler hem de adresler karşılaştırılır bu yüzden false döner
print(x is y) # adresleri aynı olduğu için true döner

"""Not: Aynı adresi gösteren 2 list değişkeni için, bir tanesinin indexteki değerlerinden biri değiştiğinde diğerinde de değişir hatırlarsan, çünkü ramdeki bilgi değişiyor. is kontrolü de adrese bakıyor, zaten aynı adresi gösteren listelerin değereri aynı olduğu için değerlerden ziyade adress bilgisi önemli burada. Aynı obje mi diye bakılıyor diyebiliriz."""

# Membership Operator: in

x = ["apple","banana"]
print("banana" in x) #banana verisi x içerisinde varmı?

name = "Ömer"
print("e" in name)
print("r" not in name)