x, y = map(int, input().split())

for i in range(1, x, 2):
    print(((y - 3 * i) // 2) * '-' + i * '.|.' + ((y - 3 * i) // 2) * '-')

print(((y - 7) // 2) * '-' + 'WELCOME' + ((y - 7) // 2) * '-')

for i in range(x - 2, -1, -2):
    print(((y - 3 * i) // 2) * '-' + i * '.|.' + ((y - 3 * i) // 2) * '-')
