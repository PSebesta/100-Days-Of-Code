# day four notes

## randomization
for you to use the random module in python we need to import that module.
```python
import random
```
there are many way to use the random module in python int, floats ect.
```python
import random
# use random module to pick random integers
# below is to select an integer between 1 and 10 

random_integer = random.randint(1, 10)

# you can also do a random float by using the random.random()

random_float = random.random()

# you can expand the random flot to include more numbers than between 0 and 1 by multipling ().random * 5) with whole nummber

randomfloat = random.random() * 5
```

## heads or tail exercise 
here is the code i came up with to solve the exercise:
```python
import random

choice = random.randint(0,1)

if choice == 0:
    print("its heads")
else:
    print("its tails")
```

## python list
a list is a data structure this is just a way to organize and store data. this is similar to a variable but the diffrence is a variable can hose 1 pice of data where a list can have many pieces of data and order to the data.

```python
states = ["delaware", "florida", "new york"]

# you can print piece of data form the list by using the index
# its important to note the the index starts at 0 and counts up from there 0,1,2,3
print(states[1])

# you can change the data in the list by selecting the index where it is store
states[2] = "pencilvania"

# you can add data to the list as well using the append function
states.append("paulworld")
```

there are many function you can use with list extend, insert, ect..

## Banker Roulette

Her is my code for the exercise
```python

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


names_integer = len(names)
choice = random.randint(0, names_integer)
who_is_paying = names[choice -1 ]

print(f"{who_is_paying} is going ot pay today!")
```

## Nested lists
this a list in a list
```python
fruits = ["stawberries", "apples", "grapes", "pears"]
vegetables = ["kale", "tomatoes", "celery"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
```

the out put of this will show double [[]] noting that its a nested list
[['stawberries', 'apples', 'grapes', 'pears'], ['kale', 'tomatoes', 'celery']]

## trasure Map

```python

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

picked_row = map[vertical - 1]

# this was a difficult one ot figure out 
picked_row = map[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

```

# final project "rock paper scissors"
check daily log for link to code
