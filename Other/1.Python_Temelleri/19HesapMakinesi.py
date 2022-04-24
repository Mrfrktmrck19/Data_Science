import os
while True:
    print("1-> Toplama")
    print("2-> Çıkarma")
    print("3-> Çarpma")
    print("4-> Bölme")
    print("5-> Bitir")
    try:
        x=int(input("Lütfen 1'den 5'e kadar bir sayi seçiniz."))
        if(not x in [1,2,3,4,5]):
            os.system("cls")
            print("Lütfen düzgün sayı gir")
        if(x==1):
            print("toplama")
        elif(x==2):
            print("Çıkarma")
        elif(x==3):
            print("Çarpma")
        elif(x==4):
            print("Bölme")
        elif(x==5):
            print("Bitiyor.")
            break
    except:
        print("Lütfen sayilari düzün giriniz")