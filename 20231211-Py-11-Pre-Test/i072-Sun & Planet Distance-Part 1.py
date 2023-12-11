# (lambda n: print(
#     'The distance between #{} planet and sun is {} AU'.format(n, ((3 * 2 ** (n - 2) if n != 1 else 0) + 4) / 10)))(
#     int(input()))

# def calculate_distance(n):
#     distance = ((3 * 2 ** (n - 2) if n != 1 else 0) + 4) / 10
#     print('The distance between #{} planet and sun is {} AU'.format(n, distance))
#
#
# planet_number = int(input())
# calculate_distance(planet_number)

n = int(input())
distance = 0.4
if n != 1:
    for i in range(1):
        distance = ((3 * 2 ** (n - 2)) + 4) / 10
print("The distance between #%d planet and sun is %.1f AU" % (n, distance))
