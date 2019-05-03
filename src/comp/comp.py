# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

print

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
a = [i.name for i in humans if 'D' in i.name]

print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
b = [i.name for i in humans if i.name[-1] == 'e' in i.name]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
import string
print("Starts between C and G, inclusive:")
c = []
#c = [i.name for i in humans if i.name[0] == 'E' in i.name]
#c = [i.name for i in i.name[0] == range('C','G') in i.name]
c = [i.name for i in humans if i.name[0] in set(string.ascii_uppercase[2:7])]

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
d = [i.age + 10 for i in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
e = [i.name + "-" + str(i.age) for i in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [tuple((human.name, human.age) for human in humans if human.age in range(27,33))]
#f = tuple((human.name, human.age) for human in humans if human.age in range(27,32)
# tuple((human.name, human.age) for human in humans)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g_copy = list(humans)
g = []
g = [Human(g_copy[0].name.upper(), g_copy[0].age + 5) for i in g_copy]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
h = [math.sqrt(i.age) for i in humans]
print(h)
