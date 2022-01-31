### Object Oriented Programming (OOP)

# class
# instance(object)
myList = [1,2,3,4,5]
print(type(list))
"""
Listenin tipine baktığında "liste tipinde bir sınıf" olduğunu göreceksin. İşte python'ın C++'tan farkı burada başlıyor. Python yüksek seviyeli bir dil aynı C#, Java gibi. Hatırlarsan o dillerde de değişken tipleri bir sınıftan türetiliyordu. Ancak C++'ta değişkenler daha temeldi. Bir sınıftan türetilmemiş, dil oluşturulurken tanımlanmıştı.

Python'da da değişkenler bir class'tan türerilerek oluşturulur. Bu yüzden herhangi bir değişken tanımlayıp nokta koyduğunda karşına methotlar çıkıyor. Yani şunu diyebiliriz: Python'da değişken türleri bir class'tan üretilmiştir.
myList.append()
myList.clear()
myList.copy()
myList.extend()
myList.index()
myList.insert()
myList.pop()
myList.reverse()
myList.remove()
myList.sort()
devamına da bakabilirsin.

Tanımlanan bir class'tan bir adet oluşturduğunda yani ramde yer ettiğindeki ismine object diyorduk. Python'da buna instance diyoruz. Mesela yukarıda list tipinden bir değişken ürettik adına da myList dedik. Bu durumda list bir class, myList ise bir object oluyor.

İşin en zevkli tarafıda kendi türlerini oluşturabilirsin!
"""

#class => PErson (name,surname,birthday,job,findAge())

class Person:
    #Class'ın içine bir şey girmeyeceksen "pass" kullanabilirsin. Boş kalan class/if/for... hata döndürür
    pass
    #class attribute
    address = "No information"
    
    #constructor()
    """
    self parametresi,class'tan türetilen bir objeyi temsil eder. Objeye bir değer aktarmak istediğimizde ve ya objenin bir attribute'una erişmek istediğimizde selfin yardımıyla istediğimizi gerçekleştirebiliyoruz. Doğrudan bir kullanım çok yapmayacağız ama arkaplanda bu işler için kullanılıyor.
    Ayrıca vermek istediğimiz parametreleride selften sonra vereceğiz. Constructor ile verdiğimiz bu parametrelere object attribute denir. C++'ta gördüğün Class içerisinde değişkene değer atamadan değişken tanımlama python'da bu yol ile yapılıyor.
    Not: self yerine this kullanabilirsin. Sana kalmış
    """
    def __init__(self,name,year): #bu değerleri obje oluştururken atamazsan hata alırsın
        #object attribute
        self.name = name
        self.year = year
        print("init methodu sen istemesende çalışır, buyrun örneği.")
    
    #method

p1 = Person(name = "Ömer", year = 1998) #p1 adında bir obje tanımlamış oldum.
p2 = Person("Ayşe",1976) #p2 adında bir obje tanımlamış oldum.
print(p1)
print(p2)   #farklı adreslerde olduğunu göreceksin.

#accessing object attribute
print(f"P1-> name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"p2-> name: {p2.name} year: {p2.year}")

#updating
p2.address = "Almanya"

print(type(p1))
print(type(p2))
print(p1 == p2) #farklı objeler olduğunu böyle anlayabilirsin.
