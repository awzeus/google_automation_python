# Fill in the gaps of the sum_squares function, 
# so that it returns the sum of all the squares of numbers between 0 and x (not included). 
# Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).  

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += n**2
    return sum

# In math, the factorial of a number is defined as the product of an integer and all the integers below it. 
# For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial 
# function return the right number.

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


#NESTED FOR LOOPS
# pairing teams home vs away

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

#creating domino values

for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end = " ")
    print()