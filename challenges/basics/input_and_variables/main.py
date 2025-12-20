"""
Exercise: 
ask the user to enter their name.
ask the user to enter their age.    
if both name and age are entered:
display:
    your name is {name}
    your name reversed is {name reversed}
    your name contains (or does not contain) spaces
    your name has {n} letters
    the first letter of your name is {first letter}
    the last letter of your name is {last letter}
el  
if nothing is entered in name or age, display "Sorry, you left fields empty."
"""

name = input('Enter your name: ')
age = input('Enter your age: ')
#if nothing is entered in name or age


if name and age:
    print(f'Your name is {name}')
    print(f'Your name reversed is {name[::-1]}')
    if ' ' in name:
        print(f'Your name contains spaces')
    else:
        print(f'Your name does not contain spaces')

    print(f'Your name has {len(name)} letters.')
    print(f'The first letter of your name is "{name[0]}"')
    print(f'The last letter of your name is "{name[-1]}"')
else:
    print("Sorry, you left fields empty.")