"""
Docstring for lesson 77
Exercise - Questions and Answers system
"""

questions = [
    {
        'Question': 'How much is 2 + 2?',
        'Options': ['1', '2', '3', '4'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5 * 5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'How much is 10 / 2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    }
]

score = 0
total_questions = len(questions)

#function to validate user input
def validate_input():
    """Validates user input and only accepts values between 0 and 3."""
    while True:
        try:
            value = int(input('Choose an option (0-3): '))
            if 0 <= value <= 3:
                return value
            print('Your answer must be between 0 and 3.')
        except ValueError:
            print('Invalid input. Please enter only numbers.')


for question_data in questions:
    print('-' * 40)

    # Getting the question
    question = question_data['Question']
    options = question_data['Options']
    correct_answer = question_data['Answer']

    print(f'Question: {question}')
    print('Options:')

    # Printing options
    for index, option in enumerate(options):
        print(f'{index}) {option}')

    # User input with validation
    user_choice = validate_input()

    # Checking answer
    if options[user_choice] == correct_answer:
        score += 1
        print('Congratulations! You got it right. :)\n')
    else:
        print('Wrong answer. :(\n')


print('\nFINAL RESULT:')
print(f'You got {score} correct answers out of {total_questions}.')
percentage = round(score / total_questions * 100, 2)
print(f'Your success rate was {percentage}%.\n')
