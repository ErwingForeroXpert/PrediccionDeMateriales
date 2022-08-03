import re
from typing import Any
from numpy import float64, NaN
from pandas import isnull

def mask_float(value: 'Any') -> float64:
    if isnull(value) or str(value) == "":
        return NaN
    else:
        try:
            if (res:=re.search(r'\-*\d*(\,|\.)*.*',str(value))) is not None:
                found = res.group(0).replace(".", "")
            else:
                found = 0
            return float64(found)
        except ValueError:
            return NaN