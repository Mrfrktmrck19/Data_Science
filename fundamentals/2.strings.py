name="Ömer Faruk"
surname="Tomurcuk"
age=23
print("This is "+name+" "+surname+". I am "+str(age))
greeting="This is "+name+" "+surname+". I am "+str(age)
print(greeting)

print(greeting[0])      #first char
print(greeting[-1])     #last char

print(len(greeting))
print(greeting[len(greeting)-1]) #last char, because index starts from 0

print(greeting[2:5])  # start from on the second index and stop at the fifth but don't handle fifth
print(greeting[2:]) #start from the second index and keep going to end.
print(greeting[:3]) #start over and go ahead to thirth index but don't handle thirth
print(greeting[2:20:5]) #start from the second index and move forward in twos


deneme="123456789"*5
print(deneme)