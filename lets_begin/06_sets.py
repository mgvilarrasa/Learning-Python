my_set = set()
my_other_set = {}

my_set = {"item1", "item2", "item3"}
my_other_set = my_set.copy()
print(my_set)
print(my_other_set)
print(len(my_set))

my_set.add("item4")
print(my_set)
my_set.remove("item3")
print(my_set)
my_set.add("item4")
print(my_set)

print("item4" in my_set)
print("item4" in my_other_set)

my_other_set.clear()
print(my_other_set)

my_other_set = {"Java", "Python", "Typescript"}
union_set = my_set.union(my_other_set)
print(union_set)
print(union_set.union({"C#", "Kotlin"}))

print(union_set.difference(my_set))
print(union_set.intersection(my_set))