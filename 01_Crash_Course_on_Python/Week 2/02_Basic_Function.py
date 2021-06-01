# Flesh out the body of the print_seconds function so that it prints the total amount of seconds
# given the hours, minutes, and seconds function parameters.
# Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

def print_seconds(hours, minutes, seconds):
    print((hours*3600)+(minutes*60)+seconds)

print_seconds(1,2,3)



# Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes,
# then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.


def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

# identify the repeated pattern and replace it with a function called month_days, 
# that receives the name of the month and the number of days in that month as parameters.
# Adapt the rest of the code so that the result is the same. 
# Confirm your results by making a function call with the correct parameters for both months listed.

def month_days(month, days):
    print (month + " has " + str(days) + " days.")
    
month_days("June",30)
month_days("July",31)


# create a function that calculates the area of a rectangle

def rectangle_area(base, height):
	area = base*height  # the area is base*height
	print("The area is " + str(area))

rectangle_area(5,6)
