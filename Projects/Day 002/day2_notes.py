# interactive excersize my solution I got the same results but my solution is more steps 
# with more practice and more knowledge I will be more efficient

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days_year = 365
weeks_year = 52
months_year = 12
max_age = 90

days_left = (max_age * days_year) - (days_year * int(age))
weeks_left = (max_age * weeks_year) - (weeks_year * int(age))
months_left = (max_age * months_year) - (months_year * int(age))

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

# Angela's solution is much cleaner and less steps 

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")