# First Duplicate Finder

This project contains Python functions that identify the first duplicated number in a list, considering the second occurrence as the duplication reference. The goal is to return the number that appears twice first, based on its second appearance. If no duplicates are found, the function returns -1.

For example:
[1, 2, 3, 3, 2, 1] -> 3  
[1, 2, 3, 4, 5, 6] -> -1

The project works with a list of integer lists and processes each internal list separately. It uses a Python set to store already visited numbers. When iterating through a list, if a number is found in the set, it means this is the first duplicated value and it is returned immediately. Otherwise, the number is added to the set and the loop continues.

Example usage:

```python
result = find_first_duplicate(list_of_integer_lists, 0)
print(result)  # -1

result_multiple_lists = process_lists(2)
print(result_multiple_lists)
# [-1, 9]
