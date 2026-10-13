
import unittest
from car_price_logic import calculate_total_price


class TestCarPriceLogic(unittest.TestCase):

    def test_total_price(self):
        self.assertEqual(
            calculate_total_price(2, 500000),
            1000000
        )

    def test_single_car_price(self):
        self.assertEqual(
            calculate_total_price(1, 250000),
            250000
        )

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            calculate_total_price(0, 500000)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_total_price(1, -500)


if __name__ == "__main__":
    unittest.main()