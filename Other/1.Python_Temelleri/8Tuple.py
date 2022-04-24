    ##Tuple-Son collection
"""
1.Kafan karışmasın. Collection dediğimiz bir küme. Bu kümeye:
List,Set,Dict ve Tuple giriyor.
2.Tuple'ın olayı: içerisindekilerin değiştirilememesi.
3.Tuple'ı genelde bir kütüphane yazıp, dönen değerlerin
değiştirilmemesi istenildiğinde kullanılır. Çoğu kütüphanede
kullandığın fonksiyonların geri dönüş değerinin tipine bak.
"""
myTuple=(0,1,2,3)
##myTuple[0]=5 ##hata verecek
print(myTuple)
print(myTuple.count(1))
print(myTuple.index(3))##3 değerinin indexini dönderecek