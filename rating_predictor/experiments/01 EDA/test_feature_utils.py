import pytest
from feature_utils import count_caps_share
import numpy as np

@pytest.mark.parametrize("test_input,expected", [('АААааа',0.5), ('Я не знаю!', 0.1),('',0),('ни одной большой буквы',0),(np.nan,None),(None,None)])
def test_count_caps_correctness(test_input, expected):
    assert count_caps_share(test_input) == expected


