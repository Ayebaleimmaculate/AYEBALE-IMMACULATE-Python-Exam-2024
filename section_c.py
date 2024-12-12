#Object-Oriented Programming (OOP) is a programming style that organizes software around objects,
# which combine data and methods.

#Modularity: Breaks programs into manageable units.
#Reusability: Encourages code reuse through inheritance.
#Maintainability: Makes code easier to update and scale.
#Flexibility: Promotes flexible and scalable software systems.

#a class is a blueprint that defines attributes and methods for creating objects. It specifies
# what properties and behaviors objects will have.

#An object is an instance of a class representing a specific entity created from the class with
# its own data.



def word_count(sentence):
    # Splits the sentence into words
    words = sentence.split()
    word_dict = {}
    
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict

# Testing the function
sentence = "python exam"
result = word_count(sentence)
print(result)



def add(a, b):
    return a + b

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

result = add(a, b)
print(f"The sum of {a} and {b} is {result}")


class Car:

    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

# Instantiate an object of the Car class
my_car = Car("Toyota", "Corolla", "Red")

print("Car Brand:", my_car.brand)
print("Car Name:", my_car.name)
print("Car Color:", my_car.color)



class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

    # Method to start the engine
    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} {self.name} has started.")

# Instantiate an object of the Car class
my_car = Car("Toyota", "Corolla", "Red")

my_car.start_engine()
