'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''

from random import randint, random
sayi = randint(1,100)
can = int(input("Kaç hak kullanmak istersiniz"))
hak = can
sayac = 0
while hak>0:
    hak-=1
    sayac += 1
    tahmin = int(input("tahmin:"))
    if sayi == tahmin:
        print(f"Doğru bildiniz. {sayac}. seferde. Toplam puanınız: {100-(100/can)*(sayac-1)}")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşşağı")
    if( hak ==0):
        print("Hakkınız bitti. Tutulan sayi: {}".format(sayi))