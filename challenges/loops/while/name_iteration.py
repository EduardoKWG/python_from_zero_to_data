"""
Iterating over strings with while

Write any string.
Use a while loop to iterate over each character of the string,
adding an asterisk '*' after each character.

Example:
'Eduardo' -> 'E*d*u*a*r*d*o*'
"""

name = "Eduardo Henrique"

# First, we get the string length dynamically. The code will still work if we change the string.
name_length = len(name)

counter = 0
final_string = ""

while counter < name_length:
    # For each character, create an intermediate string
    # that contains the character followed by '*'
    character = name[counter] + "*"
    counter += 1

    # Handle spaces without adding an asterisk
    if character == " *":
        final_string += " "
        continue

    final_string += character

print(final_string)
