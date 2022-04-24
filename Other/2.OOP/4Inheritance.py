class Animal():
    def __init__(self):
        print("Hayvan sınıfı çağrıldı")
    def method1(self):
        print("Haycan sınıfı method1 çağrıldı")
    def method2(self):
        print("Haycan sınıfı method2 çağrıldı")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Kedi sınıfı çağırıldı.")
    def meow(self):
        print("Meow")
    ##Pythond'da override bu kadar:)
    def method1(self):
        print("Kedi methot1")

MyCat= Cat()
MyCat.method1()
MyCat.meow()