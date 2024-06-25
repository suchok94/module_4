import pytest
from src.module4_1 import average

tests_values = [([], None),
                ([15], 15),
                ([i for i in range(1, 1000)], 500),
                ([-1, -2, -3, -4, -5], -3),
                ([-1, 1, -2, 2, -3, 3], 0),
                ('str', Exception),
                ([1, 2, 3, 'str'], 'TypeError'),
                ([0, 0, 0, 0, 0, 0], 0),
                ([1, 1, 1 ,1 ,1, 1], 1)
                ]

@pytest.mark.parametrize('list, expend_result', tests_values)

def test_search_average(list, expend_result):
    assert average(list) == expend_result