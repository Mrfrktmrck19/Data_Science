    ##String Slicing-String Dilimleme
fullName="Ömer Faruk Tomurcuk"
print(fullName[0])
print(fullName[fullName.__len__()-1])

"""
1.__len__() metodu stringin kaç karakte içerdiğini döndürür
bu yüzden son karaktere erişmek için -1 yazdık. Ayrıca sadece
-1 yazarsan da sondaki harfi alır.
"""
print(fullName[0]+"*****"+fullName[-1])

newString="0123456789"
print(newString[2:]) ##ilk iki indisden sonrasını alıyor. Yani 3. indisten itibaren.
print(newString[:3]) ##ilk 3 indisi alıyor.
print(newString[-2:])
print(newString[-2:])   ## gibi varyasyonları deneyebilirsin.
print(newString[2:4])   ## ilk iki indisi almıyor,3. ve 4. indisi alıyor.

    ##Step Size
print(newString[::2]) ##2 adımda bir alıyor
print(newString[1:9:2])
print(newString[::-1])  ##tersten yazdırma