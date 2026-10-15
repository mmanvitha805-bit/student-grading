Student Grading System

1. Project Description

The Student Grading System is a Python program that reads student names and marks from a CSV file and assigns grades according to predefined grading rules.

2. Grading Rules

- Marks from 80 to 100: Grade A
- Marks from 60 to below 80: Grade B
- Marks from 40 to below 60: Grade C
- Marks from 0 to below 40: Grade F
- Marks below 0 or above 100 are invalid.

3. Files

- "grading.py": Implements the grading logic.
- "students.csv": Stores student names and marks.
- "test_grading.py": Tests the grading function.
- "README.md": Contains project documentation.

4. Requirements

- Python 3
- Git

5. Run the Program

Open the terminal in the project folder and execute:

python grading.py

6. Run the Tests

Execute:

python -m unittest -v

7. Git Operations

Git is used to track changes, create feature branches, merge branches, and resolve merge conflicts.

8. Expected Result

The program should display each student's marks and corresponding grade. Invalid marks should be rejected, and the tests should verify the grading rules.