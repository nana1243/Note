import numpy as np

# https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html
"""
Return the cumulative sum of the elements along a given axis.
    Parameters : 
        a : array
        axix : 적용할 축
        dtype : data type
        out : ndarray
    Return :
        cumsum_along_axisndarray

    >>> a = np.array([[1,2,3], [4,5,6]])
    >>> a
    array([[1, 2, 3],
        [4, 5, 6]])
    >>> np.cumsum(a)
    array([ 1,  3,  6, 10, 15, 21])
    >>> np.cumsum(a, dtype=float)    
    >>> array([  1.,   3.,   6.,  10.,  15.,  21.])
    >>> np.cumsum(a,axis=0)     
    array([[1, 2, 3],
        [5, 7, 9]])
    >>> np.cumsum(a,axis=1)
    array([[ 1,  3,  6],
        [ 4,  9, 15]])

"""


a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

print(np.cumsum(a))
print(np.cumsum(a, dtype=float))
print(np.cumsum(a, axis=0))
print(np.cumsum(a, axis=1))
