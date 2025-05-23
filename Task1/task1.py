import sys

if len(sys.argv) != 3:
    print("Использование: python taks1.py <n> <m>")
    sys.exit(1)

n, m = map(int, sys.argv[1:])

if n <= 0 or m <= 0:
    print("Оба числа должны быть положительными")
    sys.exit(1)

res = []
pos = 0

while True:
    res.append(str(pos + 1))
    pos = (pos + m - 1) % n
    if pos == 0:
        break

print("".join(res))
