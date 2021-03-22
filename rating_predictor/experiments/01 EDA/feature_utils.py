import re
import pandas as pd
import numpy as np

def add_len(df: pd.DataFrame, text_columns: list) -> pd.DataFrame:
    tmp = df.copy()
    for colname in text_columns:
        tmp[colname+'_len'] = tmp[colname].str.len()
    return tmp

def count_pattern_share(pattern: str, text: str):
    if  text is np.nan or text is None:
        return None
    if not text:
        return 0
    caps = re.findall(pattern, text)
    len_caps = len(''.join(caps))
    return len_caps / len(text)

def count_caps_share(text: str) -> float:
    return count_pattern_share('[А-Я]', text)
