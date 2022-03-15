def matrix(n=1, m=None, a=0):
    if m is None:
        m = n
    return [[a for j in range(m)] for i in range(n)]

args = map(int, input().split())

m = matrix(*args)

for row in m:
    print(*row)