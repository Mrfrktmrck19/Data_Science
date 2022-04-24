    ## Hataları Ele Almak/Yakalamak-Try & Except & Else & Finally

"""
1. Try, bir hata oluştuğunda o hatayı döndürür. 
Hatanın tipine biz karar veririrz.
2. finally her zaman çağırılır
3. else, işler bizim istediğimiz gibi gittiği zaman
kullandığıız özellik.
4. Genelde ilk girişi try ile yapıp devamını else ile getiririz,
yani asıl işleri else bloğunun altında yaparız
"""
while True:
    try:
        x=int(input("İlk sayıyı giriniz"))
    except:
        print("Lütfen sayi giriniz")
        continue
    else:
        print("Teşekkürler")
        break
    finally:
        print("finally çağırıldı")