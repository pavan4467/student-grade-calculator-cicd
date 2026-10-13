
import unittest
from grade_calculator import (
    calculate_total,
    calculate_percentage,
    calculate_grade,
)


class TestGradeCalculator(unittest.TestCase):

    def test_total_marks(self):
        self.assertEqual(calculate_total([85, 90, 78, 88, 92]), 433)

    def test_percentage(self):
        self.assertEqual(calculate_percentage([80, 90]), 85.0)

    def test_grade_a(self):
        self.assertEqual(calculate_grade(95), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade(86.6), "B")

    def test_grade_fail(self):
        self.assertEqual(calculate_grade(35), "F")

    def test_empty_marks(self):
        with self.assertRaises(ValueError):
            calculate_total([])

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            calculate_total([80, 105])


if __name__ == "__main__":
    unittest.main()