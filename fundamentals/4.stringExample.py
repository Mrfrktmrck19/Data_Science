from operator import le


website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python Programlama Rehberiniz (40 saat)"

# 1- course karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))
# 2- website içinden www karakterini alın
print(website[7:10])
# 3- website içinden com karakterini alın
print(website[len(website)-3:])
print(website[-3:])
# 4- course içinden ilk 15 ve son 15 karakteri alın
print(course[:15]+"___"+course[-15:])
print(course[:15]+"___"+course[len(course)-15:])
# 5- course içerisindeki karakterleri tersten yazdırın
print(course[::-1]) #itere kısmına - yazınca tersen yazar.




name, surname, age, job= "Ömer Faruk", "Tomurcuk", 23, "AI Engineering"
#6- yukarıda verilen değişkenler ile ekrana aşşağıdaki ifadeyi yazdırınız
    #Benim adım Ömer Faruk Tomurcuk. Yaşım 23 ve mesleğim AI Enineering
print(f"Benim adım {name} {surname}. Yaşım {age} ve mesleğim {job}")
print("Benim adım {} {}. Yaşım {} ve mesleğim {}".format(name,surname,age,job))

#7- website içindeki ilk w karakterini W ile değiştir.
x = website[0:7]+"W"+website[8:]
print(x)
print(website)
