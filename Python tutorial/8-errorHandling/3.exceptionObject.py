### raising an exception - hata nesnesi oluşturma
# raise komutunu hata fırlatmak için kullanacağız.




# x = 10 
# if x>5 :
#     raise Exception("x 5'ten büyük olamaz")



# def check_password(psw):
#     import re   #regular expression kütüphanesi
#     if len(psw)<8:
#         raise Exception("Password must contain at least eight char.")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Password must contain lowercase letters.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Password must contain uppercase letters.")
#     elif not re.search("[1-9]",psw):
#         raise Exception("Password must contain numeric values.")
#     elif not re.search("_@$",psw):
#         raise Exception("Password must containt alpha numeric char <_@$>")
#     elif not re.search("\s",psw):
#         raise Exception("Password must not contain space char.")
#     else:
#         print("Geçerli parola")
# password = "12345678_Aa"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Geçerli parola ok")
# finally:
#     print("Validation tamamlandı")
# # unutma finally, except ya da else çalışsın-çalışmasın kendisi çalışır.
# # Yukarıdaki işlemde uygun olmayan bir parola girdiğimizde de finally çalışacak.





class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor.")
        else:
            self.name = name

p = Person("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",1997)
