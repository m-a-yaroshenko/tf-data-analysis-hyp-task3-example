import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import math
import scipy.stats

chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.08
    p_value = ttest_ind(x, y, alternative="greater").pvalue
    return p_value < alpha
