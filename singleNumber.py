import functools
import operator

numarray = [1, 2, 3, 3, 2, 1, 0]

def singleNumber(nums):
    return functools.reduce(operator.xor, nums)

print(singleNumber(numarray))
