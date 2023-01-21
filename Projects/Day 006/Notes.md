# Day 005 Notes

## Python functions and Karel

Defining functions: you can create your own function by using the "def" below is the basic code to do this

```python
## this part of the code is defining the function
def my_function():
    print("im awesome")
    print("this is cool")
## this part of the function is calling hte function
my_function()

```

the reeborg's world was a ton of fun learning how to create function to get through the game

## Indentation

again indentation is extremely important in python when working with creating your function if its not idented properly only part of the code will work. Anything not indented is not part of the code its reconized as something diffrent

## while Loop

A loop that will keep going as long as the condition is true

```python
# While loop: while something is true kepp running the condition
# we have a variable with the amout of times the loop should run
number_hurdles = 6
# while the number is greater than 0 continue doing the loop
while number_hurdles > 0:
    jump()
# as the while loop runs subtract 1 from the number of hurdles 
    number_hurdles -= 1
```

Hurdels challenge code with while loop and if statement

```python
# this is the turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# This is the jump hurdle function defined   
def hurdle_com():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
# use the while loop to see that we are not at the goal so continue with the code
while not at_goal():
# The if statement is checking if there is a wall in front if there is perform hurdle function
    if wall_in_front():
        hurdle_com()
# If there is not a wall in front perform the move function to move in a direction
    else:
        move()
```

Hurdles #4 my solution to the problem:

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
```
