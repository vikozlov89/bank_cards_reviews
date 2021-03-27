import pytest
from feature_utils import count_caps_share, replace_months
import numpy as np

@pytest.mark.parametrize("test_input,expected", [('АААааа',0.5), ('Я не знаю!', 0.1),('',0),('ни одной большой буквы',0),(np.nan,None),(None,None)])
def test_count_caps_correctness(test_input, expected):
    assert count_caps_share(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [('какой-то текст','какой-то текст')
                                               , ('пришел январь', 'пришел somemonth')
                                               , ('пришел февраль', 'пришел somemonth')
                                               , ('пришел март', 'пришел somemonth')
                                               , ('пришел апрель', 'пришел somemonth')
                                               , ('пришел май', 'пришел somemonth')
                                               , ('пришел Май', 'пришел somemonth')
                                               , ('пришел июнь', 'пришел somemonth')
                                               , ('пришел июль', 'пришел somemonth')
                                               , ('пришел август', 'пришел somemonth')
                                               , ('пришел сентябрь', 'пришел somemonth')
                                               , ('пришел октябрь', 'пришел somemonth')
                                               , ('пришел ноябрь', 'пришел somemonth')
                                               , ('пришел декабрь', 'пришел somemonth')]
def test_replace_months(test_input, expected):
    assert replace_months(test_input) == expected

