import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import norm

chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    X1 = np.mean(x)
    X2 = np.mean(y)
    S1 = np.var(x, ddof=1)
    S2 = np.var(y, ddof=1)
    n1 = len(x)
    n2 = len(y)
    Z_crit = norm.ppf(1 - 0.04)
    Z = (X2 - X1) / np.sqrt(S1/n1 + S2/n2)
    return True if np.abs(Z) > Z_crit else False # Ваш ответ, True или False
