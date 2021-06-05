"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
	def test_add(self):
		assert 5 == calculator.add(3, 2)

	def test_subtract(self):
		assert 5 == calculator.subtract(10,5)

	def test_mult(self):
		assert 12 == calculator.mult(3,4)

	def test_div(self):
		assert 2 == calculator.div(10,5)
