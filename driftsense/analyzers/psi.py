"""
Very small PSI calculator for demonstration.
"""
import numpy as np

def psi(expected: np.ndarray, actual: np.ndarray, buckets: int = 10) -> float:
    hist_exp, _ = np.histogram(expected, bins=buckets)
    hist_act, _ = np.histogram(actual, bins=buckets)
    pct_exp = hist_exp / hist_exp.sum()
    pct_act = hist_act / hist_act.sum()
    psi_val = ((pct_act - pct_exp) * np.log((pct_act + 1e-6) / (pct_exp + 1e-6))).sum()
    return float(psi_val)