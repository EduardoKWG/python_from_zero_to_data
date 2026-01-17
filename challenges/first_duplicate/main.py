"""
Exercise
Create a function that finds the first duplicated number considering
the second occurrence as the duplication. Return the duplicated number.

Requirements:
    The order of the duplicated number is considered from the
    second occurrence. Example:
        [1, 2, 3, 3, 2, 1] -> 1, 2 and 3 are duplicated (return 3)
        [1, 2, 3, 4, 5, 6] -> Return -1 (no duplicates)

    If no duplicates are found, return -1
"""

list_of_integer_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def find_first_duplicate(list_of_lists, inner_list_index):
    # create an empty set
    seen_values = set()

    # validate arguments
    if not isinstance(inner_list_index, int):
        return 'Index must be an integer.'

    if len(list_of_lists) <= inner_list_index:
        return 'This index does not exist in the list.'

    # check if value already exists in the set
    for value in list_of_lists[inner_list_index]:
        if value in seen_values:
            return value
        seen_values.add(value)

    return -1


# first function returns only one value from a list
result = find_first_duplicate(list_of_integer_lists, 0)
print(result)  # -1

# second function returns a list of values from multiple lists
# quantity is passed as an argument

total_lists = len(list_of_integer_lists)


def process_lists(quantity=total_lists):
    duplicated_numbers = []
    counter = 0

    while counter < quantity:
        duplicated_numbers.append(
            find_first_duplicate(list_of_integer_lists, counter)
        )
        counter += 1

    return duplicated_numbers


result_multiple_lists = process_lists(2)
print(result_multiple_lists)
# [-1, 9]