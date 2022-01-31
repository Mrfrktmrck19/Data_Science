### Object Oriented Programming (OOP)



class Person:
    pass
    #class attribute
    address = "No information"
    
    #constructor()
    def __init__(self,name,year):
        #object attribute
        self.name = name
        self.year = year
    
    #instance method
    def intro(self):
        print("Hello There. I am "+ self.name )
    def calculateAge(self):
        return 2022- self.year

p1 = Person(name = "Ömer", year = 1998) 
p2 = Person("Ayşe",1976)

p1.intro()
print(p1.calculateAge())



class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self,yaricap = 1): #default değer atadık
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    def alan_hesapla(self):
        return (self.pi*(self.yaricap**2))

c1 = Circle() # r =1
c2 = Circle(5)

print(f" c1-> çevre: {c1.cevre_hesapla()} alan: {c1.alan_hesapla()}")
print(f" c2-> çevre: {c2.cevre_hesapla()} alan: {c2.alan_hesapla()}")