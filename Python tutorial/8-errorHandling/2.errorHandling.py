# error handling => hata yönetimi



"""
x = int(input("x: "))
y = int(input("y: "))
print(x/y)

Yukarıdaki seneryoda çeşit çeşit hatalar alabiliriz. ZeroDivisionError bunlardan biri. Burada yapabileceğimiz bir şey, hata gelebilecek olan kısımları try blogğu içerisine almak olabilir. Böylelikle hatayı yakalayıp programın kapanmasına engel olabiliriz.
Hata çıkartabilecek olan kısımları try bloğunun içerisine alıyoruz, gelmesini beklediğimiz hataları ie except kısmına
"""

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# # except ZeroDivisionError:
# #     print("y için 0 girilemez.")
# # except ValueError:
# #     print("x ve y için sayısal değer girmelisiniz")
# except (ZeroDivisionError,ValueError) as e:
#     print("Hatalı bilgi girişi")
#     print(e)
# else:
#     print("Her şey yolunda")



# while True:
#     try:
#         x = int(input("x: "))
#         y = int(input("y: "))
#         print(x/y)
#     except (ZeroDivisionError,ValueError) as e:
#         print("Hatalı bilgi girişi")
#         print(e)
#     else:
#         break


while True:
    try:
        x = int(input("İlk sayıyı giriniz: "))
        y = int(input("İlk sayıyı giriniz: "))
        print(x/y)
    except Exception as e:   #child class yerine parent class kullanarak yazdırabiliriz. (sub-sup, inherit alan-veren)
        print("Hatalı giriş yaptınız. ")
        print(e)
    else:   #except bloğu çalışmazsa else bloğu çalışır
        break
    finally:
        print("Try-Except bloğu sonlandı.")
"""
=> finally'nin amacı açılan kaynakların/dosyaların kapatılmasıdır.

=> burada built-in denilen hata türlerini gördük. Yani terminalde, daha önceden dilde tanımlanmış olan hataları. Fakat kendimizin tanımladığı bir fonksiyonda hata döndürmek istersek (son kullanıcının fonksiyona yanlış parametre girmesi gibi durumlar) kendi hata classımızı oluşturmamız gerekir. Bu sayede hata oluştuğunda exception objesi oluşturulup hata ile ilgili bilgi alabiliriz.    
"""

