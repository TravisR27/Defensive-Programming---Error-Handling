# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # 2 Syntax errors , missing Parentheses () and Indentation
print ("\n") # 2 Syntax errors, missing Parentheses and Indentation

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = 24 # 3 Syntax errors - Variable incorrect written, misuse of double =, Indentation 
age = int(age_Str) # 2 Syntax error from ln 9 causing integer to not be recognised, indentation
print("I'm", int(age), "years old.") # 2 Syntax errors, Indentation, misuse of variable

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 # 2 Syntax errors, Indentation misuse, removed "" as its not a string
total_years = (age + (years_from_now)) # 2 Syntax error, Indentation misuse, Missing Parentheses ()

print ("The total number of years:", + total_years) # Logical error, print output wasnt set to total_years int, it was set as string wording

# Variable to calculate the total amount of months from the total amount of years and printing the result
total = (total_years) # Logical error, 
total_months = total * 12 + 6 # 2 Logical errors, total not defined, total * 12 only gives 324 doesnt equate for the misdsing 6 months
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # 2 Syntax errors, , missing Parentheses (), missing str

#HINT, 330 months is the correct answer

