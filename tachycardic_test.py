from tachycardic import is_tachycardic
import pytest


@pytest.mark.parametrize("a,expected", [
    ("tachycardic", True),  # exact type
    ("tacHycaRdic", True),  # acceptable typo
    ("TachyCArdic", True),
    ("tachycard ic", True),  # space typo
    ("tachyc@rd!c", True),  # punctuation typo
    ("tach3c0rdic", True),  # numeric typo
    ("4526", False),  # number input
    ("3.14159", False),  # float number input
    ("tqcgycaedis", False),  # nonsense spelling typo
    ("True", False),  # bool input
    ])
def tachycardic_test(a, expected):
    answer = is_tachycardic(a)
    assert answer == expected
