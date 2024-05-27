my_tuple = tuple()
my_other_tuple = ()

my_tuple = ("Marçal", "Gonzalez", 35)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count("Marçal"))
print(my_tuple.index(35))

my_other_tuple = my_tuple
sum_tuple = my_tuple + my_other_tuple
print(sum_tuple)
print(sum_tuple[1:3])

my_tuple = list(my_tuple)
my_tuple.append("Developer")
my_tuple = tuple(my_tuple)
print(my_tuple)