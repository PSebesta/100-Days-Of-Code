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

