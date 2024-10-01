#Loops repeat the body again and again, there are 2 types "For" and "While"
from lib2to3.pygram import python_grammar_no_print_and_exec_statement
from operator import index

#While loop
i = 0
while(i <= 7):
    if(i == 2):
        print('half way point')
    print(i)
    i+= 1 # += is equivalent to i = i + 1

print('End of While loop')
#Example
def movieMenu(index):
    movies = ['Raiders of the lost Ark','Stars Wars', 'Jurasic Park', 'The Matrix']#The list goes [0,1,2,3]
    return movies[index]

movie_names = 3 #Even tho there are 4 movie names, there are 3 cuz 0 is counted
while(movie_names > 0):
    tittle = movieMenu(movie_names)
    print(tittle)
    if(movie_names == 2):
        print('Only 2 seats remaining')
    print(movie_names)
    movie_names -= 1

#for loop
fruits = ['apple','grapes','pears']
for indexs in fruits:
    print(indexs)

a = True
b = False
c = False

if not a or b:
    print(1)
elif not a or not b and c:
    print(2)
elif not a or b or not b and a:
    print(3)
else:
    print(4)



