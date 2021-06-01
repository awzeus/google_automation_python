print("cat" > "Cat")
# "cat" is larger than "Cat"  ... In Python uppercase letters are alphabetically sorted before lowercase letters.


#The is_positive function should return True if the number received is positive, and False if it isn't. Can you fill in the gaps to make that happen?
def is_positive(number):
    if number > 0:
        return True
    else:
        return False

def is_even(number):
    if number % 2 == 0:
        return True
    return False







# The number_group function should return "Positive" if the number received is positive, 
# "Negative" if it's negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen?
def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative