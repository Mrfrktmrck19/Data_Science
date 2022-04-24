    ##try-except
def hesapla(a,b,islem):
    if islem not in "+-*/":
        return "Lütfen şu işlemlerden birini seçiniz +-*/"
    if islem=="+":
        return(str(a)+" + "+str(b)+" + "+" = "+str(a+b))
    if islem=="-":
        return(str(a)+" - "+str(b)+" + "+" = "+str(a-b))
    if islem=="/":
        return(str(a)+" / "+str(b)+" + "+" = "+str(a/b))
    if islem=="*":
        return(str(a)+" * "+str(b)+" + "+" = "+str(a*b))
while True:
    try:
        a= int(input("İlk sayiyi giriniz: "))
        
        b= int(input("İkinci sayıyı giriniz: "))
        islem=input("İşleminizi seçiniz: +-*/")
        print(hesapla(a,b,islem))

    except:
        print("Lütfen Sayileri düzgün giriniz")