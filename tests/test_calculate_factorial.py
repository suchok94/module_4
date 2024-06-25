import pytest
from src.module4_2_2 import factorial

tests_values = [(1,1),
                (0,0),
                (-1, Exception),
                (1000, 10000000),
                ('str', 'TypeError')]

@pytest.mark.parametrize('number, expend_result', tests_values)

def test_search_average(number, expend_result):
    assert factorial(number) == expend_result