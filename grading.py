import csv

def calculate_grade(marks):
    try:
      marks = float(marks)
    except (ValueError, TypeError):
     raise ValueError("Marks must be numeric")

    if marks < 0 or marks > 100:
      raise ValueError("Marks must be between 0 and 100")

    if marks >= 90:
      HEAD
      return "A"
    elif marks >= 70:
     return "B"

     return "A"
    elif marks >= 70:
      return "B"
      feature-report
    elif marks >= 40:
       return "C"
    else:
      return "F"


def read_students(filename="students.csv"):
    students = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not {"name", "marks"}.issubset(reader.fieldnames):
            raise ValueError("CSV must contain name and marks columns")

        for row in reader:
            name = (row.get("name") or "").strip()

            try:
                marks = float(row["marks"])
                grade = calculate_grade(marks)

                if not name:
                    raise ValueError("Student name cannot be empty")

                students.append({
                    "name": name,
                    "marks": marks,
                    "grade": grade
                })
            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(f"Invalid student record: {row}") from error

    return students


if __name__ == "__main__":
    try:
        for student in read_students():
            print(
                f"{student['name']}: "
                f"{student['marks']:g} marks, "
                f"Grade {student['grade']}"
            )
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error: {error}")

def calculate_grade(marks):
     try:
      marks = float(marks)
     except (ValueError, TypeError):
      raise ValueError("Marks must be numeric")

     if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

     if marks >= 80:
        return "A"
     elif marks >= 60:
        return "B"
     elif marks >= 40:
        return "C"
     else:
        return "F"