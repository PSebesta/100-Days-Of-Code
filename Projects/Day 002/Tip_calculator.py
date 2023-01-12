#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

## first need welsome message
print("Welcome to the tip calculator!")
## Next we need a input for the user to add the bill amount witha variable to store the input
total_bill = input("What was the total bill? ")
## next we need an input for the tip percentage amount and a variable to store the input
tip_amount = input("How much tip would you like to give? 10, 12, or 15? ")
## I need an input for the amount of people in the party that will split the bill and a varible to store the input
party_size = input("How many people to split the bill? ")

## going to test the inputs to make sure im getting the data
#print(total_bill, tip_amount, party_size)
## testing worked as expected 

## just realized I need a variable for the tip percentage conversion to make the math work
tip_percent = (int(tip_amount) / 100 + 1)

## created the the math to to give the amount before rounding
each_person_pays = (float(total_bill) / int(party_size)) * tip_percent
print(round(each_person_pays, 2))