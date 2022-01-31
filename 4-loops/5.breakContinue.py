### Break & Continue, break'e gelince döngü biter, continue'ya gelince o adım atlanır döngü devam eder.

name = "Ömer Faruk Tomurcuk"

for letter in name:
    if letter=="a":
        break
    print(letter)


for letter in name:
    if letter=="a":
        continue
    print(letter)