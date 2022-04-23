### While Loops

"""
Her programlama diinde döngüler aynı amaçla kullanılır, fakat detaylara inildikçe farklılaşmalar görülebilir.
For döngüsü Python'da daha çok bir listenin içine girmek için kullanılırken C++'ta neredeyse while hatta do-while
yerine bile kullanabilirsin. Bunun sebebi C++'ın çoğu özelliği/denetlemeyi programcıya bırakmasıdır.
While döngüsü burada bir koşul için kullanılır. 0'dan 100' e kadar olan sayıları bastıracasksın ve elinde bir liste
yoksa while bunun için mükemmeldir. C++'ta olsa bunu her döngü çeşidiyle yapabilirsin.
"""
x = 0
# while True: #sonsuz döngüye girer
#     print(x)

# while x<100: 
#     print(x)#burada da sonsuz döngü olur çünkü x herzaman 100'den küçük

while x<100: #0'dan 99'a kadar yazar   
    print(x)
    x+=1
x=0
while x<100:    #sadece çift sayılar bastırılır
    if x%2 ==0:
        print(x)
    x+=1
x=0
while x<100:    # sadece tek sayılar yazdırılır
    if x%2 == 1:
        print(x)
    x+=1
x=0
while x<100:
    if x%2 ==0: #çift sayılar yazdırılır
        print(f"x çift sayıdır: {x}")
        x+=1
    else:
        print(f"x tek sayıdır: {x}")
        x+=1


name = ""   #boş string false olarak değerlendirilir.
while not name.strip():     #kullanıcı bir değer girene kadar döngüden çıkılmayacak.
    name = input("lütfen bir isim giriniz: ")   #fakat burada boşluk yapıp gönderebilir. buyüzden strip ekliyoruz