def divide_two_numbers(first_number, second_number):
    my_division: int
    try:
        my_division = first_number/second_number
    except TypeError:
        print("There was a type error")
    except ZeroDivisionError:
        print("There was a divide by 0 exception")
    else: #optional
        return my_division
    finally: #optional
        print("End of function")

print(divide_two_numbers(5,2))
print(divide_two_numbers(5,0))

def divide_two_numbers_again(first_number, second_number):
    my_division: int
    try:
        my_division = first_number/second_number
    except Exception as error:
        print(error)
    else: #optional
        return my_division
    finally: #optional
        print("End of function")

print(divide_two_numbers_again(5,2))
print(divide_two_numbers_again(5,0))