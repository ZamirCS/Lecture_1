#Pyhton dictionaries
my_dictionary = {
    "school": "Valencia",
    "color": "Mustang",
    "pene": "verga",
    "grad": 1929
}
#there are two ways to retrieve values from the dictionary
x = my_dictionary["school"]
y = my_dictionary.get("pene") #.get is a function that retrieves the value, theres no diference
print(x)
print(y)

#This will retrieve the keys of the dictionary (la palabras de la izquierda)
my_keys = my_dictionary.keys()
print(my_keys)

#this is a way of change the values of the keys
my_dictionary["school"] = "Seminole State"
print(my_dictionary["school"])

#just like with keys this retrieves the values (la parte derecha)
my_values = my_dictionary.values()
print(my_values)

#this is a diferent way of changing the values of the keys
my_dictionary.update({"school": "Penelencia"})
print(my_dictionary['school'])

#this is a way to remove a key and once the key is removed all the values attached to it will too
my_dictionary.pop("pene")
print(my_dictionary)
#this is another way to remove
del my_dictionary["color"]
print(my_dictionary)

#file operation for python. "a" means append
f = open("test.txt", "a")
f.write("HOLA CHICOS")
f.close()

# r means to read the file
f = open("test.txt", "r")
print(f.read())
f.close()