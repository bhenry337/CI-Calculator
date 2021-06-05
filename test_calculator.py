"""
Unit testing calc app
"""

import calculator


class TestCalculatorApp:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)

    def test_multiply(self):
        assert 10 == calculator.multiply(2, 5)
