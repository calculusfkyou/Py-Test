a, b = map(float, input().split())
if a == 1:
    print('[%.4f]' % b)
else:
    print('[%6.2f]' % b)