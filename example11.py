import os
os.system('cls')

#Lista (Mutable)
my_list = [1, 2, 3, True, False, "Apple", 2J, 3.14, ['Mazda','Ford','Audi']]
for x in my_list:
    print(x)
my_list[1] = ['Banana','Apple']
print(my_list)

#print(my_list[8][1])
#print(type(my_list))

#Tuplas (Inmutable)
print("\n")
my_tupla = (1, 2, 3)
print(type(my_tupla))
print(my_tupla)
my_tupla[0] = 10
print(my_tupla)

#Diccionarios (Mutable)
my_data = {
    "firstname": "Jaime",
    "lastname": "Quenan",
    "city": "Pasto",
    "country": "COL"
}
print(my_data)
print(my_data["firstname"])

name = "Jaime"
for n in name:
    print(n)
print(name[0])