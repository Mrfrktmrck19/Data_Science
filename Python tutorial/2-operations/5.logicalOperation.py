# Logical Operations - Mantıksal Operatörler
from unittest import result


x,y=5,10
a = "a"
#and, both variables must be true.
result = x<6 and y>8 #true döner
result = x>5 and y<12#false döner
result = a=="a" and x == 5 #true döner

#or, if only one is true, returned true.
result = x<6 and y>8 #true döner
result = x>5 and y<12#true döner

#not, tersini yapar
deneme = not(10 <5)
print(deneme)
