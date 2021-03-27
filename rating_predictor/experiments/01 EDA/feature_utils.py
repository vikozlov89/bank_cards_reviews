import re
import pandas as pd
import numpy as np
import pymorphy2

def apply_func_to_cols(df: pd.DataFrame, columns: list, suffix: str, func) -> pd.DataFrame:
    tmp = df.copy()
    
    for colname in columns:
        tmp[colname+suffix] = tmp[colname].map(func)
    
    return tmp

def add_len(df: pd.DataFrame, text_columns: list) -> pd.DataFrame:
    return apply_func_to_cols(df,text_columns,'_len',len)

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

def count_stress_share(text: str) -> float:
    return count_pattern_share('\!', text)

def count_quest_share(text: str) -> float:
    return count_pattern_share('\?', text)

def add_share_caps(df: pd.DataFrame, text_columns: list) -> pd.DataFrame:
    return apply_func_to_cols(df, text_columns, '_caps_share', count_caps_share)

def add_share_stress(df: pd.DataFrame, text_columns: list) -> pd.DataFrame:
    return apply_func_to_cols(df, text_columns, '_caps_share', count_stress_share)

def add_share_quest(df: pd.DataFrame, text_columns: list) -> pd.DataFrame:
    return apply_func_to_cols(df, text_columns, '_quest_share', count_quest_share)

def replace_digits(text:str):
    return re.sub('\d+','somedigits',text)

def replace_variants(text, variants, replace_values)->str:
    if len(variants) != len(replace_values):
        raise Exception("varirants and replace_values must have the same length")
    if not isinstance(variants,list):
        raise Exception("varirants maust be a list")
    if not isinstance(replace_values,list):
        raise Exception("replace_values maust be a list")

    res = text
    for v, r in zip(variants, replace_values):
        res = res.replace(v,r)
    return res

def replace_months(text: str)->str:
    months = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
    return replace_variants(text, months,['somemonth']*12)

def standartize_text(text: str, analyzer: pymorphy2.MorphAnalyzer) -> str:
    res = [analyzer.normal_forms(w.lower())[0] for w in re.split("[\W\d]+",text)]
    return ' '.join(res)
