from unittest import result
import myModule as my

# result = help(my)
# result = help(my.func)

result = my.number
result = my.numbers
result = my.person["name"]
result = my.func(10)

p = my.Person()
p.speak()

print(result)