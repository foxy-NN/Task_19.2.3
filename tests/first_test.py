import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator

    def test_multiply_check(self):
        assert self.calc.multiply (self,3, 3) == 9

    def test_addition_check(self):
        assert self.calc.adding(self,100,200) == 300

    def test_division_check(self):
        assert self.calc.division(self, 625,25) == 25

    def test_subtracion_check(self):
        assert self.calc.subtraction(self,100,99) == 1
