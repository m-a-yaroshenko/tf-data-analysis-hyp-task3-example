import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int,
             y_success: int) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha=0.08
    t_stat, p_val = ttest_ind(x_success, y_success)
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return True if p_val/2 < alpha and t_stat > 0 else False # Ваш ответ, True или False
