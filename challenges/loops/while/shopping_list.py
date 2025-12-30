"""
Create a shopping list using lists.
The user must be able to add, delete, and list items.
The program must not crash due to invalid list indexes.
"""

shopping_list = []

while True:
    option = input(
        'Choose an option: [i]nsert, [d]elete, [l]ist, [q]uit: '
    ).lower()

    # input validation: only one character is allowed
    if len(option) > 1:
        print('Please type only one letter.')
        continue

    if option not in 'idlq':
        print('You must choose one of the available options (i, d, l, q).')
        continue

    # guard clause: avoid repeated checks for empty list. 
    if option in 'ld' and not shopping_list:
        print('Your shopping list is empty.')
        continue

    # insert item
    if option == 'i':
        item = input('Enter the item to add to the list: ')
        shopping_list.append(item)

    # list items
    elif option == 'l':
        for index, item in enumerate(shopping_list):
            print(index, item)

    # delete item by index
    elif option == 'd':
        index_input = input('Enter the item number to delete: ')

        try:
            index_to_delete = int(index_input)
        except ValueError:
            print('You must enter a valid number.')
            continue

        if index_to_delete not in range(len(shopping_list)):
            print('Invalid index. Please check the list.')
            continue

        print(f'Item "{shopping_list[index_to_delete]}" was removed.')
        shopping_list.pop(index_to_delete)

    # quit program
    elif option == 'q':
        break
