#Printing a string from user's input
string_input = input("Good Day. Please input a word")
print("The word is {}".format(string_input))
#String length
print("Your word length is {}".format(len(string_input)))
#String Capitalization
print(string_input.capitalize()) 
#String formatting
count=0
# String formatting
vowels = "aeiou"
contains_vowel = False
for char in string_input.lower(): 
    if char in vowels: 
        contains_vowel = True
        break  
if contains_vowel:
    print("This word contains a vowel")
else:
    print("This word does not contain a vowel")

# Checking strings through Booleans
print("string-input {}".format(bool(string_input)))  # Check if the input string is not empty  
