# (lambda sa, sb: [print(f'Similar: {len(sa)}') if (sa == sb) else print(
#     f'Different: {str(sorted(sa - sb)).replace("[", "{").replace("]", "}")} {str(sorted(sb - sa)).replace("[", "{").replace("]", "}")}')])(
#     set(map(int, input().split())), set(map(int, input().split())))

setA = set(map(int, input().split()))
setB = set(map(int, input().split()))


def compare(setA, setB):
    if setA == setB:
        print("Similar: %d" % len(setA))
    else:
        diffA = sorted(setA - setB)
        diffB = sorted(setB - setA)
        print(f'Different: {{{", ".join(map(str, diffA))}}} {{{", ".join(map(str, diffB))}}}')


compare(setA, setB)
