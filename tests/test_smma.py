"""calculate_smma must stay bit-identical to the original row loop.

jgtpy builds every Alligator line from it (9 per CDS), and consumers such as
jgwill/jgtsrc compare CDS files byte for byte across releases.
"""
import numpy as np
import pandas as pd

from jgtapy.utils import _calculate_smma_by_rows, calculate_smma


def test_bit_identical_to_the_row_loop():
    rng = np.random.default_rng(11)
    for n, period in ((3072, 377), (3072, 233), (1200, 89), (600, 13), (378, 377), (377, 377), (50, 377)):
        df = pd.DataFrame({"median": 1.1 + np.cumsum(rng.normal(0, 0.003, n))})
        fast = calculate_smma(df, period, "s", "median")["s"].to_numpy()
        rows = _calculate_smma_by_rows(df, period, "s", "median")["s"].reindex(df.index).to_numpy(dtype=float)
        assert np.array_equal(fast, rows, equal_nan=True), (n, period)


def test_a_non_positional_index_keeps_the_row_loop():
    """The row loop compares index labels with the period, so a date index
    raised TypeError before 1.9.23; it still goes through the same loop."""
    import pytest
    df = pd.DataFrame({"median": np.linspace(1.0, 2.0, 40)}, index=pd.date_range("2026-01-01", periods=40))
    with pytest.raises(TypeError):
        _calculate_smma_by_rows(df, 5, "s", "median")
    with pytest.raises(TypeError):
        calculate_smma(df, 5, "s", "median")
