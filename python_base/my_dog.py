#from Dog import Dog,Family,PetDog
import Dog
# ~ from Dog import *  不推荐

my_pet_dog = Dog.PetDog('my_pet_dog',999)

print(my_pet_dog.name)

my_pet_dog.bark()

my_pet_dog.food = ['a','b','c']

my_pet_dog.print_food()


my_pet_dog.eat_bone()


dad = my_pet_dog.family.get_dad()
print(dad)
