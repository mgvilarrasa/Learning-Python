#Fizz Buzz Challenge
def fizzBuzz():
    fizz_buzz = []
    fizz = []
    buzz = []
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            print("fizzbuzz")
            fizz_buzz.append(i)
        elif i%3 == 0:
            print("fizz")
            fizz.append(i)
        elif i%5 == 0:
            print("buzz")
            buzz.append(i)
        else:
            print(i)

#Anagram Challenge
def is_anagram(first_word, second_word):
    if len(first_word) != len(second_word):
        return False
    if first_word.lower() == second_word.lower():
        return False
    return sorted(first_word.lower()) == sorted(second_word.lower())

#Fibonacci
def fibonacci(num):
    prev = 0
    next = 1
    for i in range(0, num):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

#Prime numbers in range
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def primes_on_range(max):
    for i in range(1, max+1):
        if(is_prime(i)):
            print(i)

#Reverse string
def reverse_string(word):
    reversed_text = ""
    for i in word:
        reversed_text = i + reversed_text
    return reversed_text

fizzBuzz()
print(is_anagram("tsifr", "first"))
fibonacci(50)
primes_on_range(100)
print(reverse_string("Hello World"))