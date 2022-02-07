h_1, m_1, h_2, m_2, k = map(int, input().split())

get = h_1 * 60 + m_1
sleep = h_2 * 60 + m_2


print(max(sleep-get - k,0))