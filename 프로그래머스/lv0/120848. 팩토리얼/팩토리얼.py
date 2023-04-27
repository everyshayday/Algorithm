import math

def solution(n):
    for a in range(1, 100000000):
        if n >= math.factorial(a):
            pass
        else:
            return a-1