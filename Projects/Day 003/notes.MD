# Day 3 notes 100 days of code.

day 3 we are working on else if staements in the first video

```python
print("welcome to the rollercoaster!")
height = int(input("what is your hieght in cm? "))

if height >= 120: ## (if the height is greater than or equal to 120cm)
    print("you can ride the rollercoater")
## indentation is important with if else statements. The else is a pair with if so the indentation
## needs to be the same
else: ## if the input is less than 120 we will get this else statement
    print("Sorry, you have to grow taller before you can ride.")
```
## COMAPRISON OPERATOR:
    > GREATER THAN
    < LESS THAN
    >= GREATER THAN OR EQUAL TO
    <= LESS THAN OR EQUAL TO
    == EQUAL TO
    != NOT EQUAL TO

I figured out the code challeng

```python
number = int(input("Which number do you want to check? "))
new_number = number % 2
if new_number == 0:
    print("This is an even number.")
else:
    print("this is an odd number.")
```
nested if else statement adding more if/ else to run through diffrent inputs and get other outcomes based on the input. We can also user elif to check multiple parameters.

```python
print("welcome to the rollercoaster!")
height = int(input("what is your hieght in cm? "))

if height >= 120: 
    print("you can ride the rollercoater")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else: 
    print("Sorry, you have to grow taller before you can ride.")
```

# Code excersize BMI 2.0
This was not to bad I ran into issues with indention and my code would not run and skip over a section. I confused myself with inbeded if/ else and elif and what the indention looks like

```python
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_total = weight / (height ** 2)
bmi = round(bmi_total)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese.") 
else:
    print(f"your bmi is {bmi}, you are clinically obese.") 
```

The next excersize was a leap year checker. The tricky part about this was the way you can layout the if else statements. I didnt ralize you can put an "if" right after one another wiht out prints statements in between. 

```python
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year.")
        else:
            print("not a leap year.")
    else:
        print("leap year.")
else:
    print("no a leap year.")
```

The next coding excersise was a pizza order program. This was fun and I learned you dont need else statement in your if/ else statements.

```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"your final bill is: {bill}")
```

## logical operators
A and B: both A and B have to be true for the entire line of code to be true. if they are diffrent than the line would be false.
```python
a = 12
a > 15 and a < 13
false

a = 12
a > 10 and a < 13
true
```
C or D: this is used if you only need one condition to be true you would use the "or" if one condition or both conditions are true it will equal true. it will only be false when both conditions are false.

not E: the "not" operator reverses the condition

The code excersie was fun I had more code than the final but it worked! I do need to work on and think through how can I make the code more efficient.

```python

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()
combined_names = name1_lowercase + name2_lowercase

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

true1 = t + r + u + e
love1 = l + o + v + e


love_score = str(true1) + str(love1)
int_love_score = int(love_score)

if int_love_score < 10 or int_love_score > 90:
    print(f"Your score is {int_love_score}, you go together like coke and mentos.")
elif int_love_score >= 40 and int_love_score <= 50:
        print(f"Your score is {int_love_score}, you are alright together.")
else:
    print(f"Your score is {int_love_score}.")
```

# day 3 final project
This project was faily simple and there was a lot of freedom to make it your own. you dont have to tdo the same thing Angela did. I did a little more story telling and my if/ else statements where diffrent as well. 

[Project 3 code](https://github.com/PSebesta/100-Days-Of-Code/blob/main/Projects/Day%20003/choose%20your%20own%20adventure.py)