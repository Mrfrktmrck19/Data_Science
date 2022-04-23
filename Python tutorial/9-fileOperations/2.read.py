# try-except bloklarını özellikle dosya işlemlerinde kullanmalısın
# try:
#     file = open("thisFileDoesntExsist.txt","r") # r default, yazmana gerek yok
# except Exception as ex:
#     print("Dosya bulunamadı: ",ex)
# finally:
#     file.close()
#     print("Dosya kapatıldı.")

file = open("example.txt","r",encoding="utf-8")

###### for döngüsü ile okuma
#for i in file: # satır satır
#    print(i,end="")    #print satır sonunda 1 satır atlıyor, iptal için end kullandık





###### read fonksiyonu ile okuma
# content = file.read()   #satır satır
# print(content)
"""
Aşşağıda 2.kere ekrana bastırdığımızda boş çıktı vereceğini göreceksin. Bunun sebebi read fonksiyonu ile okuyunca cursor dosyanın en sonuna gidiyor ve başka dosyayı kapatmadığın ya da başka bir işlem yapmadığın sürece orada kalıyor. yani sen yerini değiştirmediğin srece cursor olduğu yerde kalıyor. open methodunu tekrar kullanarak verileri en baştan okuyabilirsin.
"""
# content1 = file.read()

# print("içerik 1")
# print(content1)

# content2 = file.read()

# print("içerik 2")
# print(content2)

"""
read methodu parametre girmediğinde en sona kadar okur. Numerik değer girdiğinde ise, değer kadar okur. İndex olarak değil len() olarak düşün. Fakat önce 5 karakter aldıktan sonra birde 3 karakter daha alırsak en baştan değil, cursorün en son kaldığı yerden itibaren alacağını unutma!!
"""
# file = open("example.txt","r",encoding="utf-8")
# content = file.read(6)
# print(content)


###### readline ile okuma       satır satır okur,
# file = open("example.txt","r",encoding="utf-8")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline())
# print(file.readline())


##### readlines ile okuma,   her bir satırı bir indexe atar
# file = open("example.txt","r",encoding="utf-8")
# liste = file.readlines()
# print(liste)    #her satırda, satır sonu olcuğu için \n'yi ekler :)
# file.close()