'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }
    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.
    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

ogrenciler = {}
## İlk Öğrenci
ogrenciNo = input("öğrenci numarasını giriniz")
ogrenciAd = input("öğrenci adını giriniz")
ogrenciSoyad = input("öğrenci soyadını giriniz")
ogrenciTel = input("öğrenci telefonunu giriniz")
ogrenciler[ogrenciNo] = {"ad":ogrenciAd,"soyad":ogrenciSoyad,"telefon":ogrenciTel}

## İkinci Öğrenci
ogrenciNo = input("öğrenci numarasını giriniz")
ogrenciAd = input("öğrenci adını giriniz")
ogrenciSoyad = input("öğrenci soyadını giriniz")
ogrenciTel = input("öğrenci telefonunu giriniz")
ogrenciler[ogrenciNo] = {"ad":ogrenciAd,"soyad":ogrenciSoyad,"telefon":ogrenciTel}

## Üçüncü Öğrenci
ogrenciNo = input("öğrenci numarasını giriniz")
ogrenciAd = input("öğrenci adını giriniz")
ogrenciSoyad = input("öğrenci soyadını giriniz")
ogrenciTel = input("öğrenci telefonunu giriniz")
ogrenciler[ogrenciNo] = {"ad":ogrenciAd,"soyad":ogrenciSoyad,"telefon":ogrenciTel}


print(ogrenciler)


clientNo = input("istenilen ögr no giriniz")
print(ogrenciler[clientNo])