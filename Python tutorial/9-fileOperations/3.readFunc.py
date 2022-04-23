import os
#### Dosya okuma fonksiyonları



#### with, try-except bloğu gibi çalışır, dosyayı kendi kapatır.
# write mode
with open("newFile.txt","w",encoding="utf-8") as file:
    file.write("Ömer Faruk\nTomurcuk\nYaşı 23")
# read mode
with open("newFile.txt","r",encoding="utf-8") as file:
    content =file.read()
    print(content)

# => Farklı işlemler için farklı bloklar açman gerekir.


#### tell func, cursorün konumunu yazar
#### seek func, cursorü istediğin indexe atar. read fonktan sonra kullanabilirsin
os.system("cls")    #öncekileri temizlesin diye
with open("newFile.txt","r",encoding="utf-8") as file:
    content =file.read()
    print(content)
    print(file.tell())
    file.seek(0)
    print(file.tell())
    content2 = file.read()
    print(content2)
    print(file.tell())

    print("*******************************")
    
    file.seek(10)
    print(file.tell())
    content2 = file.read()
    print(content2)
    print(file.tell())


