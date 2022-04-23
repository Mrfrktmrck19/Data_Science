x = "global x değeri"   #global scope

def func():
    x = "local x değeri" #local scope
    #bu x değerini comment yaparsak fonksiyon, bir üstteki scope'ta x değerini arayacak!
func()
#! Pythond'da bir değişken önce olduğu dizin/scope'ta aranır, eğer yoksa bir üst scope'a bakılır.
print(x)


###########################################################################
name = "Ömer Faruk"
def changeName(new_name):
    #local olarak tanımlanmış name değişkenine atandı, return yapıp globaldeki değere atarsan değişken değerini değiştirmiş olursun.
    name = new_name
    print(name)

changeName("Ada")
print(name)
###########################################################################
print("------------------------------")
name = "global string"
def greeting():
    name = "Çınar"
    def hello():
        print("hello "+name)    #buradan da gördüğün gibi bir üst dizine/scope'a baktı. Ama 1, 2 değil!
    hello()

greeting()
print(f"name son durum: {name}")

###########################################################################
print("------------------------------")
name = "global string"
def greeting():
    name = "Çınar"
    def hello():
        name = "Ada"    #bulunduğu scope'ta aradığı değişken olduğu için bir üst scope'a bakmayacak.
        print("hello "+name)  
    hello()

greeting()
print(f"name son durum: {name}")

###########################################################################
print("------------------------------")
x = 50
def test(): 
    global x
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test()
print(x)



#Kısacası: Globaldeki bir değişkeni fonksiyon içinde değiştirmek istiyorsan, return fonksiyonu kullanıp değer ataman gerekir.
