### Methods of String

message = "Hello There. My Name is Ömer Faruk Tomurcuk"
print(message.upper())
print(message.lower())
print(message.title()) # her kelimenin baş harfi
print(message.capitalize()) # ilk karakter büyük olur.


##Strip Method
message2 = "  Hello"
print(message2.strip()) #baştaki boşluk karakter(ler)ini siler.


##Split Method
message = message.split() #boşluk karakterlerine göre her stringi parçalayıp bir diziye atar.
print(message)
print(message[0])

message3 = "Hello There. My Name is Ömer Faruk Tomurcuk"
message3 = message3.split(".") #noktaya göre ayır
print(message3)

## Split ile ayrılan stringi birleştirme
message = " ".join(message)  #message'ın içindeki değerleri birleştir, bunu yaparken aralarına boşluk koy.
#message = "*".join(message)  #message'ın içindeki değerleri birleştir, bunu yaparken aralarına * koy.


##.find method
index = message.find("Ömer")
print(index) #kaçıncı indexten başladığı, eğer yoksa -1 döner

## .startwith(), içine verdiğin parametre ile başlıyorsa true döner
print(message.startswith("H"))

## .endwith()
print(message.endswith("H"))

## replace()
message = message.replace("Ömer","Omer").replace("ç","c") #birden fazlakez replace kullanabilirsin
print(message)

##center() 50 birimlik bir alan ayırıp ortalıyor. Artan tarafa isediğin şeyi yazdırabilirsin ikinci parametre yardımıyla.
#message = message.center(50)
print(message)

message = message.center(50,"*")
print(message)


## String methot search in google