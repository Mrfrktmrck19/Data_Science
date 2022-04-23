import os
#### Dosya da güncellleme yapmas

os.system("cls")
# r+ => okuma ve güncelleme yapma
# with open("example2.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# with open("example2.txt","r+",encoding="utf-8") as file:
#     file.seek(19)   #istediğin konumda güncelleme işlemi yapabilirsin
#     file.write("deneme")

# with open("example2.txt","r+",encoding="utf-8") as file:
#     print(file.read())



#*********************************************************************
# #en sona eklemek için append modunu kullanabilirsin
# with open("example2.txt","a",encoding="utf-8") as file:
#     file.write("\nErdinç Karaçizmeli")


# with open("example2.txt","r+",encoding="utf-8") as file:
#     print(file.read())
#*********************************************************************
#en başa eklemek için r+  modunu kullanabilirsin
# with open("example2.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Kişi Bilgileri:\n"+ content
#     print(content)
#*********************************************************************
# ortalarda güncelleme yapmak için
with open("example2.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    # help(list.insert)
    list.insert(1,"Ali Korkmaz\n") # 1. indexten itibaren ekler
    file.seek(0)
    for i in list:
        file.write(i)   #sayfanın en başından itibaren ekleriz. biraz amelece bir yöntem

with open("example2.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Emin Bulut\n") 
    file.writelines(list)   #listeyi direk ekler 



with open("example2.txt","r+",encoding="utf/8") as file:
    print(file.read())