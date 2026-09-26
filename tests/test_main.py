import unittest
import main

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.expenses = [
            {"date": "2026-09-01", "category": "Food", "amount": 100.0, "description": "Lunch"},
            {"date": "2026-09-02", "category": "Travel", "amount": 50.0, "description": "Bus"}
        ]

    def test_total(self):
        self.assertEqual(main.calculate_total(self.expenses), 150.0)

    def test_average(self):
        self.assertEqual(main.calculate_average(self.expenses), 75.0)

    def test_empty_average(self):
        self.assertEqual(main.calculate_average([]), 0)

if __name__ == "__main__":
    unittest.main()
