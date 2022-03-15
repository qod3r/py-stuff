def transpose(m):
    # hehe
    m_T = list(zip(*m))
    m.clear()
    m += m_T


m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

transpose(m)
for line in m:
    print(*line)
