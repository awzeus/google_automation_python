# Complete the function by filling in the missing parts.
# The color_translator function receives the name of a color,
# then prints its hexadecimal value. Currently, it only supports
# the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


# Students in a class receive their grades as Pass/Fail. 
# Scores of 60 or more (out of 100) mean that the grade is "Pass".
# For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". 
# Fill in this function so that it returns the proper grade.

def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail





def format_name(first_name, last_name):
	if len(first_name) >0 and len(last_name) > 0:
		string = "Name: " + last_name + ", " + first_name
	elif len(first_name) >0 or len(last_name) > 0:
		if len(first_name) > 0:
			received_name = first_name
		else: received_name = last_name
		string = "Name: " + received_name
	else:
		string = ""

	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string