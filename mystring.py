x = "Cyberscripter's python academy"
print(x)
print(type(x))
x = 10
print(type(x))
x = 'Cyberscripter\'s python academy'  # "\" is escape character
print(x)

print(x.upper())
print(x.lower())
print(x.isdigit())
print("python is good languate".title())  # This is going to capitalize first char of every word to capital
#print(x.casefold()) # casefold() is similar to lower() but is advanced version of lower() and converts even some special characters to lowercase
# Eg 'B' (beta) which is German letter and its lower case is 'ss'
print(f"Value of count() {x.count('pyt')}")

print(x.isdigit())
print(x.isalnum())
print(x.isalpha())
print(x.isdecimal())

multilinestr = ''' This is my multiline string, this is first line
and this is second line'''
print(multilinestr)

print(f"Ex startswith {'python is a good language'.startswith('good')}")  # to check if string starts with specific substring
print(f"Ex endswith {'python is a good language'.endswith('age')}")  #endswith()  # to check if string ends with specific substring
print(f"Ex replace {'python is a good language'.replace('good', 'bad')  }")  #replace() # to replace part of a string
#split() # to split a string
#strip() # to trim whitespaces
#join()  # to append new letters to string,
#find()  # to find position of a substring