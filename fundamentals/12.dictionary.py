### Dictionary-Sözlük
# Key-Value şeklinde çalışır, diğer programlama dillerindekine benzer

license_plates= {"İstanbul":34,"İzmir":35}
print(license_plates)
print(license_plates["İstanbul"])   #value değerini döndürür.

license_plates["Ankara"]=6  #listeye eleman ekleyebiliyoruz
print(license_plates)
#license_plates["İzmir"] = "otuz beş" #değer güncelleyebiliyoruz

users = {
    "Ömer Faruk":23,
    "Ayşe":45
}

users = {
    "Ömer Faruk": {
        "age":23,
        "email":"mrfrktmrck@gmail.com",
        "phone":"5523610912",
        "roles":["admin","producer"]
    },
    "Ayşe":{
        "roles":["mother","designer","cooker","user"],
        "age":45
    }
}
print(users["Ömer Faruk"]["email"])
print(users["Ömer Faruk"]["roles"][0])