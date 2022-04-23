### Inheritance - Kalıtım

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print("Person object was created")
    def who_am_i(self):
        print("I am a person.")
    def eat(self):
        print("Person is eating.")
class Student(Person):
    def __init__(self,fname,lname,number):
        super().__init__(fname,lname)  # Person.__init__(self)
        self.number = number
        print(f"name: {self.fname} {self.lname}")
        print("Student was created.")
    #override
    def who_am_i(self): 
        print("I am a student")
"""
Yukarıdaki constructor tanımlamasında student constructor'ı person constructor'ını ezer. Fakar Kalıtım'ın zaten espirisi Sup classın özelliklerini alması olduğu için pek bir mantığı yok. Sadece methotlar çalışır

def __init__(self,fname,lname):
    super().__init__(fname,lname)
bu şekilde tanımlamamızın amacı: def initin içini zaten tanımlıyoruz ona okeyiz, super().__init__() içerisinde tanımlamamızın sebebi ise 
self.fname = fname
self.lname = lname
şeklinde tanımlama yerine kalıtım aldığı objeye gönderip atama yaptırtıyoruz.

"""

p1 = Person("Ömer","Faruk")
s1 = Student("Ahmet","Turan",10) 

print(f"Name: {p1.fname} Last Name: {p1.lname}")
print(f"Name: {s1.fname} Last Name: {s1.lname}")
print("******************************************")
p1.who_am_i()
s1.who_am_i()
print("******************************************")
p1.eat()
s1.eat()
print("******************************************")
print(f"Name: {s1.fname} Last Name: {s1.lname} number: {s1.number}")


#normalde classları ayrı tanımlamak çokta programcılığa uygun değildir fakat öğrenme aşamasında olduğum için okunabilir olması adına yapıyorum.
class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch
    def who_am_i(self):
        print(f" I am a {self.branch} teacher")
    
t1 = Teacher("Alperen","Yıldırım","Social Informations")
t1.who_am_i()