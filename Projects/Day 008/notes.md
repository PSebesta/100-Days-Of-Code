# Day 008 Notes

## Function with inputs

we can create functions and in the () we can pass a variable
parameter = is the name of the data that is being passed in 
argument = is the actual value of the data

```python


# Basic function
def greet():
    print("hello")
    print("how do you do")
    print("how is the weather")

greet()

# Function with a input

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do you do {name}")

greet_with_name("cousin it")

```

## positional vs keyword arguments

position arguments is the defualts for function where the argument is in the () is what will be printed out

```python
## function with more than 1 input

def with_greet(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
# below is a positional aegument if below was switched scotland, jack scottland would be printed for name
# and jack for the location
with_greet("jack", "scotland")

```

Keyword arguments is more specific and you defining exactly what the parameter argument will be

```python

## function with more than 1 input

def with_greet(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
# below keyword argument where we are specifying the data in the parameter so no matter where they are in
# the () it will print the way you want it
with_greet(name = "jack",location = "scotland")

```

## coding exercise 1

```python

import math
def paint_calc(height, width, cover):
    area = height * width
    num_cans = area / cover
    print(f"You'll need {math.ceil(num_cans)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

```

## coding exercise 2

```python
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime == False
    if is_prime:
        print("its a prime number.")
    else:
        print("its not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)

```
