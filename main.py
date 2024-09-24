#instead of doing food1 food2 food3
#instead of using one variable for multiple values you can use lists, example:
food = ["queso","huevo","leche"]
print(food)
print(food[0])
print(food[1])
print(food[2])
print()
#values can be replaced by making a new variable
food[0] = 'jamon'
print(food[0])
print(food)
print()
# the len() command will tell how many values are in the list
print(len(food))
print()
# the nameOfList.append command will add items to existing lists
food.append('carne')
print(food)
print(food[3])
print(len(food))
print()
# values can also be inserted by using the .insert command
food.insert(1,"naranja")
print(food)
print(food[1])
print(len(food))
print()
# Elements can be removed by using two commands, either .PoP or .Remove
food.pop(2) #if there's no index the last value of the list will be removed
print(food)
print(len(food))
print()
food.remove('carne') #the spelling its important since it has to be the exact same value
print(food)
print(len(food))
print()
# List are allowed to have duplicate values in the same variable
food.append('naranja')
print(food)
print()
# if the remove command is used when there are duplicates the first value from the left to right will be removed
food.remove('naranja')
print(food)
print()
# You can also clear the whole list with the command clear
food.clear()
print(food)
print()
#tuples:they act as a list but these are unchangable so everything in the list cant be changed, but values can still be added
cars = ('ford','toyota','bently')
print(cars)
print(cars[2])
print(len(cars))
cars = cars + ('mercedes',) #this is the way of adding more values to the tuple 
print(cars)
print()
#cars[2] = 'rolls royce' | this command wouldnt work on this
#there's a way to convert a tuple into a list and then to a tuple back to remove a value ex:
temp = list(cars)
temp.remove('mercedes')
cars = tuple(temp)
print(cars)
# A tuple is basically a way to lock a list 


