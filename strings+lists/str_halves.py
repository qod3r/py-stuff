import math

s = input()

a = s[:math.ceil(len(s)/2)]
b = s[len(s) - math.ceil(len(s)/2) + 1:]

res = b + a
print(res)
