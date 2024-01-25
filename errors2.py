# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Name error, Lion not been defined "" Syntax error
animal_type = "cub"
number_of_teeth = 16
# 1 logic error: the output structure is not correct, it should say "it is a cub " and "it has 16 teeth" not "it is 16 and it has a cub" 1 Syntax error, syntax error: missing f before the string to indicate a formatted string
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" 

print (full_spec) # Syntax error, missing parentheses in call to print ()

