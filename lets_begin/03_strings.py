first_string = "Hello"
second_string = "World"

print(first_string + " " + second_string)

print("First Line\nSecond Line")
print("\tTab line")
print("\\tScape stuff")

name, surname, age = "Marçal", "Gonzalez", 35
print("My name is {} {} and I'm {} years old".format(name, surname, age))
print("My name is %s %s and I'm %d years old" %(name, surname, age))
print(f"My name is {name} {surname} and I'm {age} years old")

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
language_slice = language[0:3]
print(language_slice)
language_slice = language[2:]
print(language_slice)
language_slice = language[-2]
print(language_slice)
reversed_language = language[::-1]
print(reversed_language)

print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))