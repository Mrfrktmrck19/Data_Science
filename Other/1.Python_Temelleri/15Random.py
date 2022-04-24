    ## Random sayı oluşturma
from hashlib import new
from random import randint

print(randint(0,100)) ##0 ile 100 arası random sayı üretiyor


newList= list(range(0,10))
print(newList[randint(0,9)])

from random import shuffle
##shuffle/ karıştır
shuffle(newList)    ##listeyi karıştırır
print(newList)