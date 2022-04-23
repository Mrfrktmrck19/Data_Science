import random

result = dir(random)    ##içindeki methotları gösterir.
# result = help(random)

result = random.random()    #0.0-1.0 arası
result = random.random()*100    #0.0-1.0 arası'nın 100 ile çarpmı
result = random.uniform(1,10) #1-10 arası floating point
result = int(random.uniform(1,10)) #1-10 arası int
result = random.randint(1,100)  #1-100 aras int


names = ["Ali","Ömer","Ahmet","Selin","Tansu"]
result = names[random.randint(0,len(names)-1)]
result = random.choice(names) ##listeden random eleman seçmek için tasarlanmış metot


liste = list(range(10))
result = liste
random.shuffle(liste)   #listeyi karıştırır.

liste =list( range(100))
result = random.sample(liste,3) #liste'den 3 tane random eleman getirecek
print(result)
