# print('Hello World')

# # daatypes
# # int -> 1 2 3 4 5 6 7 8 9 10
# # float -> 1.1 2.2 3.3
# # string -> 'Hello World'
# # boolean -> True or False

# # variables
# x = 1
# y = 2
# z = 3   # this is a comment
# print(x + y + z)

# # operators
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)

# # strings
# print('Hello World')
# print("Hello World")
# print('Hello "World"')
# print("Hello 'World'")
# print("Hello \"World\"")
# print("Hello \nWorld")
# print("Hello \tWorld")  

# # boolean
# print(True)
# print(False)

# # if else
# if x > y:
#     print('x is greater than y')
# else:
#     print('x is less than y')   

# #if else ladder
# if x > y:
#     print('x is greater than y')
# elif x < y:
#     print('x is less than y')
# else:
#     print('x is equal to y')

# # loops
# while x < y:
#     print(x)
#     x = x + 1

# for i in range(10):
#     print(i)

# for i in range(10, -1,-1):
#     print(i)


# for i in reversed(range(10)):
#     print(i)

# functions
def add(x, y):
    return x + y

print(add(1, 2))

def num(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(num(5))

#data structures
# list
# tuple
# set
# dictionary

# list

#Write a program to decide whether to wear sunglasses or not based on the weather.

weather = 'sunny'

if weather == 'sunny':
    print('wear sunglasses')
else:
    print("don't'") 

#Create a list of five of your favorite snacks and print each snack using a loop.

snacks = ['cookies', 'farsan', 'aloo bhujiya', 'biscuits', 'choot']
print(snacks)

def reverse_string(text):
    return text[::-1]
reversed_text = reverse_string('chootpagal')
print(reversed_text)

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(3)

#Write a function to calculate the tip at a restaurant based on the bill.

def calculate_tip(bill):
    return bill * 0.2

bill = 100
tip = calculate_tip(bill)
print(bill + tip)

#Write a function that takes a name and age, and tells you how old the person will be in 5 years.

def age (name, age):
    return name + ' will be ' + str(age + 5) + ' in 5 years'
print(age('mayank', 28))

#Write a function to generate a random superhero name (e.g., "Captain Code" or "Super Python").

import random   
def superhero():
    adjectives = ['Captain', 'Incredible', 'Amazing', 'Wonderful', 'Super']
    nouns = ['Code', 'Python', 'Hulk', 'Batman', 'Spiderman']
    return random.choice(adjectives) + ' ' + random.choice(nouns)
print(superhero())

import time

def countdown(seconds):
    while seconds > 0:
        print(f"{seconds} seconds remaining...")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
print(countdown(5))

#Write a function to simulate flipping a coin (heads or tails).
import random
def flip_coin():
    return random.choice(['heads', 'tails'])
print(flip_coin())

#Create a function that checks if a word is an anagram of another (e.g., "listen" and "silent").
def anagram(word1, word2):
    return sorted(word1) == sorted(word2)
print(anagram('listen', 'silent'))

