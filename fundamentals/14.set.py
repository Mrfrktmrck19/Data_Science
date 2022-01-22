### Sets, en büyük farkı, indexlenemez olması ve bir eleman sadece bir kez eklenebilir.
fruits = {"orange","apple","banana"}

print(fruits)

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape"]) #birden falz eleman ekleyeceğin zaman bir liste içerisinde gönderebilirsin
fruits.remove("mango")  #silme
fruits.discard("apple") #silme
fruits.clear()  #tüm elemanlar siliinir
#? Not: pop methodu ile silme yapılabilir fakat hangi elemanın silineceği belli olmadığından tavsiye edilme<
#? çünkü pop methotu index ile silme yapan bir fonksiyon iken setlerde index olmaz.
myList = [1,2,3,4,5,6,7,7,7,7]
print(set(myList))