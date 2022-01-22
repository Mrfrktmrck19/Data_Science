### Methods of List - Listenin Methotları
numbers = [1,10,5,6,79,56,10]
letters = ["a","g","h","s","y","a","b"]

val = min(numbers)  #listedeki en küçük sayıyı buldu
val = max(numbers)  #listedeki en büyük sayıyı buldu

val = min(letters)
val = max(letters)

val = numbers[3:6]
val = numbers[3:6]
val = numbers[::2]
print(val)

numbers[3] = 12 #listenin bir elemanını değiştirebiliriz!
numbers.append(49)  #listeyeen sona yazdığın değeri ekler
numbers.insert(3,78)    #belirtilen indexe belirttiğin sayıyı insert eder, 3 ve 3ten sonrakileri bir sağa kaydırır.
numbers.insert(-1,52)   #en sondan bir önceki indexe ekler, en sına eklemek için appendi kullan

numbers.pop()   #en sondaki elemanı siler değer vermezen, index değerini vererek istediğin yerdeki değeri silebilirsin.
numbers.remove(10)  #girdiğin "value"yu siler, index değil bak! eğer girdiğin değer yoksa hata döndürür. iki tane
                    #aynı değerden varsa ilk bulduğunu siler.

numbers.sort()  #küçükten büyüğe sıralar,harfler varsa a dan z ye
numbers.reverse()   #yukarıdakinin tersi.


print(numbers.count(10))    #10 değerinden kaç adet olduğunu gösterir.
print(letters.count("a"))


numbers.clear() #bütün elemanları siler
print(numbers)
