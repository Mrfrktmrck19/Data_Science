    ##While Loop- While Döngüsü
"""
Koşul sağlandığı sürece devam eden döngü tipi.
"""
x=0
while x<10:
    print(x)
    x+=1
##======================================================
myList=[0,1,2,3,4,5,6,7,8,9]
while(3 in myList):
    print("Hala var")
    myList.pop()
print("Artık yok")

##======================================================
numara=0
while(numara<5):
    if numara==4:
        break
    print(numara)
    numara+=1
##======================================================
numara=0
while(numara<15):
    print("Güncel deger: "+str(numara))
    print(f"Güncel deger: {numara*5}")
    numara+=1