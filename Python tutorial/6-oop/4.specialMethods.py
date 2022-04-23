from operator import le


myList = [1,2,3]
myString = "Ömer Faruk Tomurcuk"

print(len(myList))
print(len(myString))

class Movie:
    def __init__(self,title,director,duration):
        self.title = title
        self.directior = director
        self.duration = duration
# m = Movie()
# print(len(m))   # Movie class'ı için bir len tanımlanmadığından hata döner
# print(type(m))


m = Movie("Film","Stanley Kubrick","120")


"""
Burada şunu anlamalısın, len, str gibi methotlar yeni tanımladığın classlarda çalışmayabilir. Bunun sebebi o methodun o classta tanımlanmamış olmasıdır. O methodu tanımlayarak ya da override ederek kullanabiirsin.
"""