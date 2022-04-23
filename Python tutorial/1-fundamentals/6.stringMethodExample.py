
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python Programlama Rehberiniz (40 saat)"

#1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
x = " Hello World "
print(x.strip()+"test")
print(x.lstrip()) #soldaki ifadelri sil
print(x.rstrip()) #sağdaki ifadeleri sil
#2- website içerisinde sadikturan haricindeki her karakteri silin.
x = website.find("sadikturan")
x = website[x:21]
print(x)

y = website.lstrip("htp:/").rstrip(".com")
print(y)

z = website.strip("wmoc.htp:/")
print(z)

#3- course karakter dizisinin tüm karakterlerini küçük harf yapın
print(course.lower())

#4- website içerisine kaç adet a harfi vardır? count(a)
print(website.count("a"))
print(website.count("a",0,10))#0 ile 10 arasında .com varmı
#5- website www ile başlayıp com ile bitiyor mu?
print(website.startswith("www"))
print(website.endswith(".com"))

#6- website içerisinde .com ifadesi var mı ?
print(website.find(".com")) #varsa pozitif değer döner
print(website.find(".com",0,10)) #belirlenen alanlar arasında mevcutmu


print(course.find("Python"))    #soldan ilk pythonu bulur
print(course.rfind("Python"))   #sağdan ilk pythonu bulur

#Not: find yerine index methodu da kullanılabilir. Farkı, index bir sonucu bulamayınca hata döner.

#7- course içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(course.isalpha()) # false döner çünkü numerik değerler de var
deneme = "Hello".isalpha()
print(deneme)
# deneme2= "123456".isdigit()
# print(deneme2)
#8- "Contents" ifadesini satırda 50 karakte içine yerleştirip sağ ve soluna * ekle.
x = "Contents".center(50,"*")
x = "Contents".ljust(50,"*") #sola yaslar
x = "Contents".rjust(50,"*") #sağa yaslar
print(x)

#8- course karakter dizisindeki tüm boşluk karakterlerini "-" le değiştir
print(course.replace(" ","-",5)) ##sadece 5 tanesi için bunu uygular
print(course.replace(" ","")) ##tüm boşluk karakterlerini siler

#9- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.
print("Hello World".replace("World","There"))

#10- course karakter dizisini boşluk karakterlerine göre ayır.
print(course.split())