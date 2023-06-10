# Problem Statement: Cyclic shift

# A large binary number is represented by a string A of size N and comprises of 0s and 1s. You must perform a cyclic shift on this string. The cyclic shift operation is defined as follows:

# If the string A is [A0, A1,..., An-1], then after performing one cyclic shift, the string becomes [A1, A2,..., An-1, A0].

# You performed the shift infinite number of times and each time you recorded the value of the binary number represented by the string. The maximum binary number formed after performing (possibly 0) the operation is B. Your task is to determine the number of cyclic shifts that can be performed such that the value represented by the string A will be equal to B for the Kth time.

# Input format:

# First line: A single integer T denoting the number of test cases For each test case: First line: Two space-separated integers N and K Second line: A denoting the string

# Output format:

# For each test case, print a single line containing one integer that represents the number of cyclic shift operations performed such that the value represented by string A is equal to B for the Kth time.

# Code:

import math
def value(s):
    u = len(s)
    d = 0
    for h in range(u):
        d = d + (int(s[u-1-h]) * math.pow(2, h))
    return d


t = int(input())
for i in range(t):
    x = list(map(int, input().split()))
    n = x[0]
    k = x[1]
    a = input()
    v = 0
    for j in range(n):
        a = a[1:] + a[0]
        if value(a) > v:
            b = a
            v = value(a)
    ctr = 0
    cou = 0
    while ctr < k:
        a = a[1:] + a[0]
        cou = cou + 1
        if a == b:
            ctr = ctr + 1
    print(cou)
