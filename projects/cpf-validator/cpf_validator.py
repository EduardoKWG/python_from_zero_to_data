"""
Challenge: Validate the first and second check digits of a CPF number.

CPF FIRST CHECK DIGIT CALCULATION:
Step by step:
1) Multiply each of the first 9 digits of the CPF by a countdown from 10 to 2, 
then sum the results.
Example: 746.824.890-70 (74682489070)

   7   4   6   8   2   4   8   9   0
*  10  9   8   7   6   5   4   3   2
-------------------------------------
   70  36  48  56  12  20  32  27  0

2) Sum all results
   Total sum: 301

3) Multiply the previous result by 10
   301 * 10 = 3010

4) Get the remainder of the division by 11
   3010 % 11 = 7

If the result is greater than 9:
   the digit becomes 0
Otherwise:
   the digit is the result itself

The first CPF check digit is 7.

///////////////////////////////////////////////////////////////////////
CPF SECOND CHECK DIGIT CALCULATION:

1) Multiply each of the first 10 digits of the CPF (the first 9 digits plus 
the first check digit) by a countdown from 11 to 2, then sum the results.
Example: 746.824.890-70 (74682489070)

   7   4   6   8   2   4   8   9   0   7
*  11  10  9   8   7   6   5   4   3   2  <--- FIRST CHECK DIGIT
-----------------------------------------
   77  40  54  64  14  24  40  36  0   14

2) Sum all results
   Total sum: 363

3) Multiply the previous result by 10
   363 * 10 = 3630

4) Get the remainder of the division by 11
   3630 % 11 = 0

If the result is greater than 9:
   the digit becomes 0
Otherwise:
   the digit is the result itself

The second CPF check digit is 0.
"""

import re

while True:
    # User input
    input_cpf = input("Enter a CPF number: ")

    # Remove formatting characters
    cpf_clean = input_cpf.replace(".", "").replace("-", "").replace(" ", "")

    # Alternative approach using regex:
    # cpf_clean = re.sub(r'[^0-9]', '', input_cpf)

    # Validate length
    if len(cpf_clean) != 11:
        print("The CPF must contain exactly 11 digits. Try again.")
        continue

    # Validate numeric content
    if not cpf_clean.isdigit():
        print("The CPF contains invalid characters. Use numbers only.")
        continue

    # Block CPFs with all repeated digits
    if cpf_clean[0] * len(cpf_clean) == cpf_clean:
        print("This CPF is invalid because all digits are the same.")
        continue

    # Extract the first nine digits
    first_nine_digits = cpf_clean[:9]

    # ---------- First check digit calculation ----------
    countdown_1 = 10
    sum_digits_1 = 0

    for digit in first_nine_digits:
        if countdown_1 <= 1:
            break
        sum_digits_1 += countdown_1 * int(digit)
        countdown_1 -= 1

    product_1 = sum_digits_1 * 10
    remainder_1 = product_1 % 11

    first_check_digit = remainder_1 if remainder_1 <= 9 else 0
    print(f"The first check digit is {first_check_digit}.")

    # ---------- Second check digit calculation ----------
    countdown_2 = 11
    sum_digits_2 = 0
    first_ten_digits = first_nine_digits + str(first_check_digit)

    for digit in first_ten_digits:
        if countdown_2 <= 1:
            break
        sum_digits_2 += countdown_2 * int(digit)
        countdown_2 -= 1

    product_2 = sum_digits_2 * 10
    remainder_2 = product_2 % 11

    second_check_digit = remainder_2 if remainder_2 <= 9 else 0
    print(f"The second check digit is {second_check_digit}.")

    # ---------- Final validation ----------
    cpf_check_digits = cpf_clean[-2:]

    if (
        str(first_check_digit) == cpf_check_digits[0]
        and str(second_check_digit) == cpf_check_digits[1]
    ):
        print("Your CPF is valid.")
    else:
        print("Your CPF is invalid.")

    break
