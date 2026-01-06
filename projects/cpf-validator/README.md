# CPF Validator (Python)

This project is a **CPF (Cadastro de Pessoas Físicas) validator** implemented
in Python. It verifies whether a CPF number is valid by calculating and
comparing its two check digits using the **Modulus 11 algorithm**.

## Features

- Removes CPF formatting characters (`.` and `-`) that are usual at this register
- Validates input length and numeric content
- Blocks invalid CPFs with all repeated digits (e.g. `11111111111`)
- Calculates the first and second check digits
- Compares calculated digits with the provided CPF
- Returns a clear valid or invalid result

## Algorithm

The CPF validation process consists of:

1. Using the first 9 digits to calculate the first check digit
2. Using the first 9 digits plus the first check digit to calculate the second
3. Applying a weighted sum with a countdown multiplier
4. Using modulo 11 to determine each check digit
5. Validating the CPF by comparing calculated and original digits

## How to Run

1. Make sure you have Python installed (version 3.x)
2. Clone this repository
3. Navigate to the project folder:
   ```bash
   cd projects/cpf-validator
