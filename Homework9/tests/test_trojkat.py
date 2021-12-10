import unittest
from unittest.mock import patch

from Homework9.trojkat import Trojkat


class Mock:
    bok1 = 3
    bok2 = 4
    inputs = [bok1, bok2]
    index = 0

    @classmethod
    def provide_input(cls, text):
        result = Mock.inputs[Mock.index]
        Mock.index += 1
        return result


class TestTrojkat(unittest.TestCase):
    @patch('trojkat.input', wraps=Mock.provide_input)
    def test_Trojkat(self, mock_class):
        bok1 = 3
        bok2 = 4
        result = Trojkat()
        assert result.bok1 == bok1
        assert result.bok2 == bok2




