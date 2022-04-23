### Comparison Operators - Karşılaştırma Operatörleri

from unittest import result


a,b,c,d = 5,5,10,4
password = "12345"
username = "omer"

result = a==b
result = (a==c)

result = (username == "omer")   #login girişi
result = (password == "54321")

result = (a!=b) #a ile b eş değilse true dönecek
result = (a!=c)

result = a<c    # a c den küçük mü
result = a>c    # c a'dan küçük mü
result = a<=c   # a c'den küçük ya da eşit mi
result = a>=c   # c a'dan küçük ya da eşit mi

result = True ==1   #true
result = False ==0  #true

result = True ==0   #false
result = False ==1  #false
print(result)

