import pytest
from app.calculator import Calculator

#
# def multiply(x, y):
#     return x * y
#
# def test_multiply_calculate_correctly():
#     assert multiply(2, 3) == 6

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    # def test_multiply_calculation_failed(self):
    #     assert self.calc.multiply(self, 2, 3) == 5


    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 3) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 4, 3) == 7