from ast import Str
from operator import truediv
from re import X


print("We are starting.")
print("5+3 =",5+3,"asdasdasdasdasd")
print("5+3.5 =",5+3.5)
print("5+3.0 =",5+3.0)
print("(10+2.7)*5+6 = ",(10+2.7)*5+6)

## Math operations *, /, +, -, **(üs alma), %(mod), //(tam bölme)
print("10/7 = ",10/7)
print("10%7 = ",10%7)
print("10//7 = ",10//7)
print("-10/7 = ",-10/7)
print("-10%7 = ",-10%7)
print("-10//7 = ",-10//7)

## variable definition
x=1
y=10
name="Ömer"
isWorking=True
a,b,c,d=1,2,3,4   #çoklu değişken tanımlaması yapılabilir

num1="10"
num2="20"
print(num1+num2) #string concatenation

##variable type conversion
x= input("ilk sayıyı giriniz:")
y= input("ikinci sayıyı giriniz:")
print(type(x))
print(type(y))
result = int(x)+int(y)
print(result)
print(type(result))

#int to float
x=1
x=float(x)
print(x)
print(type(x))
#float to int
x=1.5
x=int(x)
print(x)
print(type(x))
#string to int, ayrıca int to string, float to string, string to float'ta yapabilirsin.
x="5"
x=int(x)
#bool to str
isOnline = True
isOnline = str(isOnline)
print(type(isOnline))
print(isOnline)
#bool to int
isOnline = True
isOnline = int(isOnline)
print(type(isOnline))
print(isOnline)