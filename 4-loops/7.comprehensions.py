### Comprehensions, for ve while döngüsüne alternatif olarak kullanılır.

import numbers

#1.yol
for i in range(11):
    print(i)
#2.yol
numbers = [x for x in range(10)]
print(numbers)

#1.yol
for i in range(10):
    print(i**2)
#2.yol
numbers = [x**2 for x in range(10)]
print(numbers)



#1.yol
for i in range(10):
    if i%3==0:
        print(i**2)
#2.yol
numbers = [x**2 for x in range(10) if x%3==0]
print(numbers)




years = [1988,1993,1998,2000]
ages = [2022-year for year in years]
print(ages)



results = [x if x%2==0 else 'TEK' for x in range(1, 10)]
print(results)



result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)