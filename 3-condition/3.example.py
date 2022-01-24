# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 
name = input("Adınızı giriniz: ").strip()
age = int(input("Yaşınızı giriniz: "))
educationStatus = input("Eğitim durumunuzu giriniz: ").lower().strip()

# if (yas>=18):
#     if (egitim=='lise' or egitim=='üniversite'):
#         print(f'{isim} ehliyet alabilirsin.')
#     else:
#         print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz.')
# else:
#     print(f'{isim} ehliyet alamazsın yaşın tutmuyor.')

if (age >=18) and (educationStatus == "lise" or educationStatus=="üniversite"):
    print(f"Sayın {name}, ehliyet alabilirsiniz.")
elif(age >=18)and(educationStatus != "lise" or educationStatus!="üniversite"):
    print(f"Sayın {name}, ehliyet almak için yaşınız tutuyor fakar eğitim durumunuz yetersiz.")
elif (age <18) and (educationStatus == "lise" or educationStatus=="üniversite"):
    print(f"Sayın {name}, ehliyet almak için eğitim durumunuz yeterli fakar yaşınız tutmuyor.") ##yersen :)
else:
    print(f"Sayın {name}, ehliyet için hem yaşınız hemde eğitim durumunuz yetersiz.")

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

firstResult = float(input("İlk sınav notunu giriniz: "))
secondResult = float(input("İkinci sınav notunu giriniz: "))
totalResult = (firstResult+secondResult)/2

if(85<=totalResult) and (100>=totalResult):
    print(f"Ortalamanız {totalResult}, dönem sonu sonutunuz 5")
elif(70<=totalResult) and (84>=totalResult):
    print(f"Ortalamanız {totalResult}, dönem sonu sonutunuz 4")
elif(55<=totalResult) and (69>=totalResult):
    print(f"Ortalamanız {totalResult}, dönem sonu sonutunuz 3")
elif(45<=totalResult) and (54>=totalResult):
    print(f"Ortalamanız {totalResult}, dönem sonu sonutunuz 2")
elif(25<=totalResult) and (44>=totalResult):
    print(f"Ortalamanız {totalResult}, dönem sonu sonutunuz 1")
else:
    print(f"Ortalamanız {totalResult}, dönem sonu sonutunuz 0")

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün
import datetime as dt
print("*********************************************************************************")
date = input("Aracınızın yola çıkış tarihini yıl/ay/gün (2022/09/12) formatında giriniz")
date = date.split("/")
firstOut = dt.datetime(int(date[0]),int(date[1]),int(date[2]))
currentTime = dt.datetime.now()
print(f"First out: {firstOut}")
print(f"Current time: {currentTime}")

difference = (currentTime - firstOut).days
print(difference)

if(difference <=365):
    print("1. servis aralığı")
elif(difference>365) and (difference<=365*2):
    print("2. servis aralığı")
elif(difference>365*2) and (difference<=365*3):
    print("3. servis aralığı")
else:
    print("Hatalı süre")