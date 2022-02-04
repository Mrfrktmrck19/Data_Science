#YÖNTEM 1,
import math
# import math as mt

#value = dir(math)   #dir function provides to display functions that are inside the math module
#value = help(math)  #help function provides to display definitions of the methods
#value = help(math.factorial) #it just displays what the factorial method does.



value = math.sqrt(49)
value = math.factorial(5)
value = math.floor(5.9) #aşşağıya doğru yuvarlar
value = math.ceil(5.1) #yukarı daoğru yuvarlama yapar
print(value)

#YÖNTEM 2
from math import * 
from math import factorial 
from math import sqrt
"""
bu yöntemle modülün tamamını ya da bir kısmını (zaten genellikle de bir kısmını katmak isteriz) projemize dahil edebiliriz. Modülün tamamını yukarıdaki gibi dahil edersek, math ön ekini kullanmadan methotları çağırabiliriz aynı static fonkiyonları kullanır gibi.

Not: ilgili dosyada aynı isimde iki fonksiyon varsa en son hangsi tanımlanmış ise onu geçerli sayar.
"""