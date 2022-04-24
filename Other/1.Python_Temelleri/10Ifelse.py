    ##If-else
if 3>2:
    print("True değer döner")

if 4>5:
    print("True değer döner")
else:
    print("False değer döner")
##============================================================
yas=23
if yas<13:
    print("Çocuk")
elif yas<20:
    print("Genç")
else:
    print("Yetişkin")
##============================================================
a=10
b=15
c=20

if a>b and a>c:
    print("En büyük değer: a")
elif b>a and b>c:
    print("En büyük değer: b")
elif c>a and b<c:
    print("En büyük değer: c")
##============================================================
k=1
l=2
m=3

if k<l or k<m:
    print("K değeri ya hepsinden küçük, ya da l değerinden küçük ya da m değerinden küçük. ")

##============================================================
karakterCanli=False
if karakterCanli==True:
    print("Karakter hayatta")
else:
    print("Karakter ölü")

if karakterCanli:
    print("Karakter hayatta")
else:
    print("Karakter ölü")


if karakterCanli==True:
    print("Karakter hayatta")
else:
    print("Karakter ölü")


if karakterCanli==True:
    print("Karakter hayatta")
else:
    print("Karakter ölü")

if not karakterCanli==True:
    print("Karakter ölü")
else:
    print("Karakter hayatta")

if not karakterCanli:
    print("Karakter ölü")
else:
    print("Karakter yaşıyor")
##============================================================
isim="Ömer"
if isim=="ömer":
    print("Eşitmiş")
else:
    print("Değilmiş")

if "er" in isim:    ##in, içerisinde o değer varmı diye bakıyor.
    print("varmış")
else:
    print("yokmuş")
##============================================================
listem=[0,1,2,3,4,5,6,7]
if 10 in listem:
    print("Var")
else:
    print("Yok")

if 0 in listem:
    print("Var!!")
else:
    print("Yok!!")
##============================================================
mydict={"muz":250}
if "muz" in mydict.keys():
    print("muz var")
else:
    print("muz yok")
if 250 in mydict.values():
    print("250 var")
else:
    print("250 yok")