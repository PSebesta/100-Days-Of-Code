# Day 5 notes

This days final project is a password generator!

## Loops

for loops:
you can add multiple instrustion to the loop to be carried out and indentation is extrememly important when using loops.

```python
# this will print all the data in the list works similiar to if/ else
fruits = ["apple", "peach", "Pear"]
# for fruit in fruits list print all fruit in the list
# "fruit" is creating a variable that each time the loop runs a diffrent fruit from the list is added to "fruit"
for fruit in fruits:
    print(fruit)
# we can add more action in the loop we need to make sure we are indented to keep it part of the loop
    print(fruit + " Pie")
# this will print the fruit like before "Apple" than print "Apple Pie"

```
Average height exercise:

```python
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

## you will need a variable to pass the value to for the for loop
total_height = 0
for total in student_heights:
    total_height = total_height + total


number_of_students = 0
for number in student_heights:
    number_of_students += 1


print(round(total_height / number_of_students))

```
The High score exercise:

```python
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

## according to the exercise we are trying to replicate the Max function in python using a for loop

highest_test_score = 0
for score in student_scores:
# where I went wrong is I didnt add a if statemnent I need to remeber to use what I learned before.
# we are checking if the score is higher than highest_test_score
    if score > highest_test_score:
# after the check has happend than the score will go to the variable highest_test_score
        highest_test_score = score
print(f"The highest score in the class is: {highest_test_score}")

```

## For loops and the range

this is a loop using hte range function to you can step through a set range of numbers.

```python
# For loop with range
## the first 2 number are the range it will step through if you want a range of 1 - 10 you need to add 1
## the 3rd number is if you want to skip a few numbers so the 3 would do every 3rd number
for number in range(1, 11, 3):
    print(number)

# if you want to know the total of a range lets say 1 - 100 we would do:
total = 0
# we need to add one so we can get 1- 100
for number in range(1, 101):
    total += number
print(total)
```

## adding even numbers exercise

```python
# what I did 
total_number = 0
for number in range(2, 101, 2):
    total_number += number
print(total_number)

# The 2nd solution that was offered by the instrutor

total_number = 0
for number in range(1, 101,):
    if number % 2 == 0:
        total_number += number
print(total_number)
```
## The fizzBuzz

```python

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

```

