### Assigment Operations -- Atama Operatörleri
x = 5 
y = 10
z = 15

x,y,z = 5,10,15
print(x,y,z)


x,y = y,x
print(x,y,z)

# x = x+5
# x += 5

# x = x-5
# x -= 5

# x = x*5
# x *= 5

# x = x/5
# x /= 5

# x = x%5
# x %= 5

# x = x//5
# x //= 5



values=(1,2,3)  
x,y,z=values    #böyle bir atama mevcuttur. tuple'daki eleman sayısı ile değişken sayısı aynı olmalı
print(x,y,z)    

values=(1,2,3,4,5,6)  
x,y,*z=values    #z bir liste oldu
print(x,y,z)   
print(type(z))