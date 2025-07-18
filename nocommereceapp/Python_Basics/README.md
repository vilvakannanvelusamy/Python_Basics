# Project Title: Count Numbers with Exactly 9 Divisors

## Overview
This project provides a solution to count the numbers less than or equal to a given positive integer `n` that have exactly 9 divisors. The main logic is implemented in the `main.py` file, while utility functions are provided in `utils.py`. The project also includes a set of unit tests to ensure the correctness of the implementation.

## Functionality
- **Count Numbers with Exactly 9 Divisors**: The core functionality is encapsulated in the function `count_numbers_with_nine_divisors(n)` located in `count_nine_divisors/main.py`. This function takes an integer `n` and returns the count of numbers with exactly 9 divisors.

## Project Structure
```
Python_Basics
├── count_nine_divisors
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests
│   └── test_count_nine_divisors.py
└── README.md
```

## How to Run the Program
1. Clone the repository to your local machine.
2. Navigate to the `Python_Basics` directory.
3. Run the main program using the command:
   ```
   python count_nine_divisors/main.py
   ```

## How to Execute Tests
To run the tests, navigate to the `tests` directory and execute:
```
python -m unittest test_count_nine_divisors.py
```
or if you are using pytest:
```
pytest test_count_nine_divisors.py
```

## Requirements
- Python 3.x
- Any additional libraries required for testing (e.g., `unittest` or `pytest`)

## Author
[Your Name]