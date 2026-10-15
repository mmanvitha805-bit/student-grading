import unittest
from grading import calculate_grade, read_students


class TestGrading(unittest.TestCase):

    def test_grade_categories(self):
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(70), "B")
        self.assertEqual(calculate_grade(50), "C")
        self.assertEqual(calculate_grade(20), "F")

    def test_grade_boundaries(self):
        self.assertEqual(calculate_grade(80), "A")
        self.assertEqual(calculate_grade(60), "B")
        self.assertEqual(calculate_grade(40), "C")
        self.assertEqual(calculate_grade(0), "F")

    def test_invalid_marks(self):
        for marks in (-1, 101):
            with self.subTest(marks=marks):
                with self.assertRaises(ValueError):
                    calculate_grade(marks)

    def test_csv_records(self):
        students = read_students("students.csv")
        self.assertEqual(len(students), 5)


if __name__ == "__main__":
    unittest.main()