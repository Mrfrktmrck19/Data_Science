# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
car_list=["Bmw","Mercedes","Opel","Mazda"]
# 2-  Liste Kaç elemanlıdır ?
list_len = len(car_list)
print(list_len)
# 3-  Listenin ilk ve son elemanı nedir ?
print("First value: {} and last value: {}".format(car_list[0],car_list[list_len-1]))
# 4-  Mazda değerini Toyota ile değiştirin.
# car_list[-1]= 'Toyota'
car_list[list_len-1] ="Toyota"
# 5-  Mercedes listenin bir elemanı mıdır ?
result = "Mercedes" in car_list
print(result)
# 6-  Listenin -2 indeksindeki değer nedir ?
print(car_list[-2])
# 7-  Listenin ilk 3 elemanını alın.
print(car_list[0:3])
print(car_list[:3])
print(car_list[-4:-1])

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
car_list[-2:]=["Toyota","Renault"]
print(car_list)
# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
car_list = car_list + ["Audi","Nissan"]
print(car_list)
# 10- Listenin son elemanını silin.
del car_list[-1]
print(car_list)
# 11- Liste elemanlarını tersten yazdırınız.
print(car_list[::-1])
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA=["Yiğit","Bilgi",2010,[70,60,70]]
studentB=["Sena","Turan",1999,[80,80,70]]
studentC=["Ahmet","Turan",2010,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)