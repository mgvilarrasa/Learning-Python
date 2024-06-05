from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values(first, second, f_sum):
    return f_sum(first + second)

print(sum_two_values(1,2, sum_one))
print(sum_two_values(1,2, sum_five))

#CLOSURES
def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_closure = sum_ten()
print(add_closure(25))

def sum_three(sum_value):
    def add(value):
        return value + 10 +sum_value
    return add
    
add_closure = sum_three(1)
print(add_closure(25))
print(sum_three(2)(5))

#BUILT-IN
numbers = [1, 2, 3, 4, 11, 12, 13, 14]
#Map
def multiply_by_two(number):
    return number*2

print(list(map(multiply_by_two, numbers)))
print(list(map(lambda number: number * 5, numbers)))

#Filter
def filter_greater_than_ten(number):
    return number > 10

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

#Reduce
def sum_two_values(first, second):
    return first + second
print(reduce(sum_two_values, numbers))