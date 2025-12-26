import random

"""
Word Guessing Game.
The user must guess a secret word by typing one letter at a time.
The game reveals correct letters and counts the number of valid attempts.
"""
#list of possible secret words
words = ['monkey', 'tiger', 'mantis', 'viper', 'crane', 'panda']

secret_word = random.choice(words)

# Converts the secret word letters into '*'
guessed_word = '*' * len(secret_word)

attempts = 0
tried_letters = ''

# Loop until the secret word is fully guessed
while guessed_word != secret_word:
    user_input = input('Enter a letter: ').lower()

    # Validates if the user typed only one letter
    if len(user_input) != 1 or not user_input.isalpha():
        print('Please enter only ONE valid letter!')
        continue

    # Checks if the letter was already tried
    if user_input in tried_letters:
        print(f'You have already tried the letter "{user_input}". Try another one.')
        continue

    tried_letters += user_input
    attempts += 1

    # Iterates through the secret word
    # enumerate -> returns both index and value
    for i, letter in enumerate(secret_word):

        # Uses slicing to replace '*' with the correct letter.
        # Strings are immutable in Python.
        if user_input == letter:
            guessed_word = (
                guessed_word[:i]
                + user_input
                + guessed_word[i + 1:]
            )

    print(f'Word = {guessed_word}')

print(f'Congratulations! You guessed the word "{secret_word}" in {attempts} attempts.')
