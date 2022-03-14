### Functions as Parameters - Fonksiyonları parametre olarak gönderme.


def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplaction(a,b):
    return a*b

def division(a,b):
    return a/b


def func(f1,f2,f3,f4,islem_adi):
    if islem_adi =="toplama":
        print(f1(2,3))
    elif islem_adi =="çıkarma":
        print(f2(2,3))
    elif islem_adi =="çarpma":
        print(f3(2,3))
    elif islem_adi =="bölme":
        print(f4(2,3))

    else:
        print("geçersiz işlem...")

func(addition, subtraction, multiplaction, division, "toplama")
func(addition, subtraction, multiplaction, division, "çıkarma")
func(addition, subtraction, multiplaction, division, "çarpma")
func(addition, subtraction, multiplaction, division, "bölme")
func(addition, subtraction, multiplaction, division, "carpmaa")