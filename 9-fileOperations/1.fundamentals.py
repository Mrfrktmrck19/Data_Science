## To create or open folder we use open() method.
## use of: open(file_name,file_access_mode)
## file_access_mode: it indicates for what purpose you opened the file.

# "w" that means write mode. if there is no folder, it creates currently directory
# "a" that means append mode.
# "x" that means create mode. If already folder is existing, it raise an error.
# "r" that means read mode. This mode is default.

#If we don't indicate folder address, Python looks for the file in its directory. 
#open("example.txt","r") #for example, py will look for on current directory.


# file = open("example.txt","w") #buradan bir parametre dönecek, bak bakalım neymiş
# print(file)
# file.close()

"""
Dönen değerde dosya adı, dosyanın açılış modu ve yazılan karakter tiplemesi (encoding) mevcut. 

Not:Türkçe karakter kullanacaksan cp1254'ü utf ile değiştirmeni tavsiye ederim.

open() methodunu bir değere atamamızın sebebi: dönecek olan objeyi tutmak/yakalamak. Çünkü dosya üzerinden işlemler yapacağımızda bize yarayacak. (Dosyaya veri yazma-silme, açılan dosyayı kapatma vs.)

Not2: Açtığın her dosyayı kapatman gerekir. Çünkü yazdığın uygulamayı kapattığın zaman dosya kapanmamış olabilir. Dosyanın açılıp kapanması uygulamayla bağlantısız çünkü. Boşa kaynak harcaması ve içerisinden veri çalınabilmesi gibi durumlara karşı kapatmalıyız.

Not3: Path verirken "\" yerine "/" kullanmalısın, hata verir.
"""
#farklı adreslerdeki dosyalara erişim sağlayabiliriz.
# file = open("c:/Users/mrfrk/Desktop/newfile.txt","w")
# file.close()



#write modu, dosya içeriğini siler, yeniden ekleme yapar. Varolan bilgilerin üstüne ekleme yapmaz
# file = open("example.txt","w",encoding="utf-8")
# file.write("Ömer Faruk Tomurcuk")
# file.close()


#append modu, dosya içeriğini silmeden, var olan bilgilere ek olarak veri girmek istediğimizde kullandığımız moddur. Kaç kere çalışıtıtrsan o kadarkez yazar senin girdiklerini.
# file = open("example.txt","a",encoding="utf-8")
# # file.write(" 23 CS")
# # file.write("\n23 CS")
# # file.write("\n23 CS\n")
# file.close()


#sadece dosyayı oluşturup bırakacaksan create modu
# file = open("example2.txt","x",encoding="utf-8")
#aynı dosyadan varsa tekrar oluşturmaz, hata döndürür.