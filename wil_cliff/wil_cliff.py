# wil_cliff/wil_cliff.py
from scipy.stats import wilcoxon
from cliffs_delta import cliffs_delta

def wil_cli(ls1, ls2):
    statistic, p_value = wilcoxon(ls1, ls2)
    d, res = cliffs_delta(ls1, ls2)

    return p_value, d, res