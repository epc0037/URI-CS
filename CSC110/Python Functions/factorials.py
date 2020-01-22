# CSC 110 - Spring 2016 - Section 1
# Week 4 (Functions) - Class Activities (Tuesday)
# Examples: Combinations

# This program computes n choose r (n | r)
# (n | r) = n!/((n-r)!*r!)

# Solution 1 without functions

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

# compute n!
fact_n = 1
i = 1
while i <=n:
    fact_n = fact_n * i
    i = i + 1

# compute r!
fact_r = 1
j = 1
while j <= r:
    fact_r = fact_r * j
    j = j + 1

# compute (n-r)!
x = n - r
fact_x = 1
k = 1
while k <=x:
    fact_x = fact_x * k
    k = k + 1

# compute n!/((n-r)!*r!)
result = fact_n/ (fact_x * fact_r)
print(result)
