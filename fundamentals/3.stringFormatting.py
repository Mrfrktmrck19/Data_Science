###String Formatting - String Formatlama
name = "Ömer Faruk"
surname = "Tomurcuk"
print("My name is {} {}".format(name,surname))
print("My name is {0} {1}".format(name,surname))    # values that inside bracktes are default. (0 ,1)
print("My name is {1} {0}".format(name,surname))    
print("My name is {nm} {sr}".format(nm=name,sr=surname))    
print("My name is {} {} {}".format(name,surname,"36"))    
print("My name is {} {} {}".format(name,surname,40))    

num1 = 25.123456789
print("{}".format(num1))    #don't have to convert to int
print("{n:20.5}".format(n=num1))    #first number defines number of spaces, second number defines how many indexes print on


print(f"My name is {name} {surname}")   #second way to print on screen