x, y = map(int, input().split())
time = x * 60 + y
time_ans = time + 150
h = str(time_ans // 60 % 24)
m = str(time_ans % 60)
h = h.zfill(2)
m = m.zfill(2)
print('%s:%s' % (h, m))
