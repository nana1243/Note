import numpy as np
import pandas as pd

"""
DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwds)
    Apply a function along an axis of the DataFrame.
    Param:
        - func :각 row or column에 행할 연산함수
        - axis :row or column에 적용할 것 인지
    Return:
        - Series or DataFrame
"""
df = pd.DataFrame([[4, 9]] * 3, columns=["A", "B"])
print(df)
print(df.apply(np.sum, axis=0))
print(df.apply(np.sum, axis=1))
