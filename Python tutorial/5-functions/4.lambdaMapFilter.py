### LAmbda Expressions - Map - Filter


#Aşşağıdaki iki fonksiyonda aynı işlevi görmektedir.
def square(num):
    return num**2

def square(num): return num**2  

"""
Tek bir sayı göndermek yerine bir liste göndermek istediğimiz de tabiki parametre kısmına *args girebiliriz. Fakat bunun yerine kullanabileceğimiz başka bir alternatfimiz daha var: map methodu. Bu methodun amacı, bir fonksiyona/methoda parametre olarak verceğin değer(ler)i map methodunun kendisinin verip fonksiyonu kendisinin çalıştırmasıdır.
Not: Burada method adı yazdıktan sonra () koymuyoruz.
"""
numbers = [2,2,3,4,5,6,7,8,9]
result = list(map(square,numbers))  #map methodundan dönen veriyi listeye çeviriyoruz,
print(result)                       #alternatifi olarak for döngüsü ile de atayabilirsin ama bu daha rahat

for item in map(square,numbers):
    print(item)


"""
map fonksiyonunun içine fonksiyon da yazabiliriz. Buna Lambda Expression denir. Özellikle ufak tefek işler yapan fonksiyonları Lambda expression ile yapmak hem daha kolay hem daha okunaklı kod yazmanızı sağlar.
list (map(lambda num: num**2,numbers)) => num, bildiğin değer tanımlama. Return yazmana gerek yok.  
"""
result = list (map(lambda num: num**2,numbers))
square = lambda num: num**2 #tanımlamayı böyle de yapabiliriz.
print(square(3))


"""
Map fonksiyonu bir built-in fonksiyonudur, bize pyhton ile birlikte gelir. Genel amacı ise yukarıda dediğimiz gibi bir fonksiyona parametreler verip bir değer veya değerler döndürmesini sağlamak. Ancak biz seçeceğimiz parametrelerde bir filtreleme işlei uygulamak isteyebiliriz. 
"""

def check_even(num):
    return num%2 ==0
print(list(filter(check_even,numbers))) #filtreden true alan değerler geçer
print(list(map(check_even,numbers)))    #map'te true false döner

check_even = lambda num : num%2==0
print(list(filter(check_even,numbers)))