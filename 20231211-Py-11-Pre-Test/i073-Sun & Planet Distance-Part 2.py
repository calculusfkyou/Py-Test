# aucal = (lambda a, b: (1 + aucal(a, b + 1) if 3 * 2 ** (b - 2) < a else 1) if a >= 0.4 else 0);(lambda n: print('Among {0:.1f} '.format(62500 * n) + 'AU has about {} planets in solar system.'.format(aucal((62500 * n * 10) - 4, 2))))(eval(input()))


def calculate_planets(a, b):
    if a >= 0.4:
        if 3 * 2 ** (b - 2) < a:
            return 1 + calculate_planets(a, b + 1)
        else:
            return 1
    else:
        return 0


n = eval(input())
total_au = 62500 * n
adjusted_au = (total_au * 10) - 4
planet_count = calculate_planets(adjusted_au, 2)
# print('Among {0:.1f} AU has about {1} planets in solar system.'.format(total_au, planet_count))
print('Among %.1f AU has about %d planets in solar system.'%(total_au, planet_count))
