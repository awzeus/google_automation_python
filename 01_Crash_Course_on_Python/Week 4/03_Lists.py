# Using the "split" string method from the preceding lesson, 
# complete the get_word function to return the {n}th word from a passed sentence. 
# For example, get_word("This is a lesson about lists", 4) should return "lesson", 
# which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1. 

def get_word(sentence, n):
    	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")
print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing



# The skip_elements function returns a list containing every other element from an input list, 
# starting with the first element. Complete this function to do that, using the for loop to iterate through the input list.
def skip_elements(elements):
    	# Initialize variables
	new_list = []
	i = 0
	# Iterate through the list
	for element in elements:
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(element)
		# Increment i
		i += 1
	return new_list
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


#ENUMERATE FUNCTION, same as previous function but using enumerate
def skip_elements_2(elements):
	new_elements = []
	for index, element in enumerate(elements):
		if (index + 1) % 2 != 0:
			new_elements.append(element)
	return new_elements
print(skip_elements_2(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements_2(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


# LIST COMPREHENSIONS
multiples_of_7 = [ x*7 for x in range(1,11) ] # [7, 14, 21, ..., 70]
multiples_of_3 = [x for x in range(0,101) if x % 3 == 0]

#odd_numbers_in_range
def odd_numbers(n):
    	return [x for x in range(0,n+1) if x % 2 != 0]
print(odd_numbers(11))

languages = ["Python", "Perl", "Ruby", "JavaScript", "Kotlin", "Java", "Go"]
lengths = [len(language) for language in languages] # [6, 4, 4, 10, 6, 4, 2]


