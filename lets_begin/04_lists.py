my_list = list()
my_other_list = []

print(len(my_list))

my_list = [1, 22, 35, 22, 18]
print(my_list)
print(len(my_list))

my_other_list = [1, 25.58, "This is a text", True, 18]
print(my_other_list)
print(len(my_other_list))
print(my_other_list[2])
print(my_other_list[-1]) #last element
print(my_other_list[-3]) #negative from last element
print(my_other_list[-5])

print(my_list.count(22))
print(len(my_list))
print(my_list + my_other_list)

my_list.append(105)
print(my_list)
my_list.pop() #can receive index as argument
print(my_list)
my_list.remove(22)
print(my_list)
my_list.insert(1, 200)
print(my_list)
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)
print(my_list.index(200))
del my_list[4]
print(my_list)
my_list.clear()
print(my_list)
my_list = my_other_list.copy()
print(my_list)
print(my_list[1:2])