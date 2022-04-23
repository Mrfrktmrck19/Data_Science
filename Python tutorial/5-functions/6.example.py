## Bankamatik Uygulaması

hesapA = {
    "ad": "Ömer Faruk Tomurcuk",
    "hesapNo": "12345",
    "bakiye": 3000,
    "ekHesap": 2000
}

hesapB = {
    "ad": "Ayşe Karaçizmeli",
    "hesapNo": "456789",
    "bakiye": 4000,
    "ekHesap": 5000
}

def paraCek(hesap,miktar):  #hesap objesi, çekilmke istenen para miktarı
    print(f"Merhaba {hesap['ad']}") #tek-çift tırnağa, birden fazla kez kullaancağın yerlerde dikkat et.

    if hesap["bakiye"] >=miktar:
        print("Paranızı alabilirsiniz")
    else:
        toplam = hesap["bakiye"]+hesap["ekHesap"]
        if toplam>=miktar:
            print("Bakiye yetersiz. Ancak ek hesap ile bilrikte paranızı çekebilirsiniz.")
            ekHesapKullanimi = input("Kullanmak iste misiniz? (e/h)")
            if ekHesapKullanimi == "e":
                hesap["ekHesap"] = 0
                hesap["bakiye"] = toplam-miktar
                print(f"Para çekme işleminiz gerçekleşti, yeni bakiyeniz: {hesap['bakiye']}")
                return hesap
            else:
                print("Sen bilirsin, biz değil sen kaybedersin hadi eyv.")
                return hesap
        else:
            print("Bakiye yetersiz.")
            return hesap




hesapA = paraCek(hesapA,4000)
##===========================================================================================================
SadikHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(SadikHesap, 3000)

print('*****************')

paraCek(SadikHesap, 2000)