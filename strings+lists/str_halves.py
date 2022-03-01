import math

s = input()

a = s[:math.ceil(len(s)/2)]
b = s[len(s) - len(s)//2:]

res = b + a
print(res)
