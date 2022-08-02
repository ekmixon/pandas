"""
Helpers for sharing tests between DataFrame/Series
"""

from pandas import DataFrame


def get_dtype(obj):
    return obj.dtypes.iat[0] if isinstance(obj, DataFrame) else obj.dtype
