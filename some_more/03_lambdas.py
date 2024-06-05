sum_two_numbers = lambda first_number, second_number: first_number + second_number
print(sum_two_numbers(5,12))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(48,5))

def sum_constants(value):
    return lambda first_value, second_value: first_value + second_value + value
print(sum_constants(5)(2,3))