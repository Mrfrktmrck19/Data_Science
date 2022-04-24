    ## Önemli bazı methotlar
"""
1. Bir şeyleri denerken/test ederken ürekli deneme
yapmak için bir liste oluşturuyoruz. Bunun çok daha 
kolay yolu var. Range...
"""
myList=[0,1,2,3,4,5,6,7,8,9]

print(range(10))
print(type(range(10)))

print(list(range(10)))
print(type(list(range(10))))

print(list(range(0,10,2))) ##0 dan başla, 10'a kadar git(10 dahil değil), 2 şer ilerle

    ##enumerate
index=0
for num in list(range(15)):
    print(f"güncel numara: {num}, index: {index}")
    index+=1
##enumerate burada indexte tuttuğu için kullanılıyor.
for num in enumerate(list(range(0,15,3))):
    print(num)
    print(type(num))## çünkü değiştirilmemesi isteniyor

for (index,num) in enumerate(list(range(0,15,3))):
    print(f"numara:{num}, index{index}")