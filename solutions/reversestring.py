# List to string
# For and While loop
# reversed, range, len functions

originalstr = "mystring"
reversedstring = ""
for i in originalstr:
    reversedstring = i + reversedstring
print(reversedstring)

reversedstring = ""
strlen = len(originalstr)
for i in reversed(range(0, strlen)):
    reversedstring = reversedstring + originalstr[i]
print(reversedstring)

# Using slicing
print(originalstr[::-1])

# Using reversed() and list() function

reversedstring = ""
for ele in list(reversed(originalstr)):
    reversedstring = reversedstring + ele

print(reversedstring)