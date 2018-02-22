import math

a, b = map(lambda x: float(x) / 2,
           input('enter lengths of larger rec: ').split(' '))

c, d = map(lambda x: float(x) / 2,
           input('enter lengths of smaller rec: ').split(' '))
f = math.hypot(c, d)

ans = math.pow(2 * d, 2) <= math.pow(
    b - math.sqrt(math.pow(f, 2) - math.pow(a, 2)), 2) + math.pow(
        a - math.sqrt(math.pow(f, 2) - math.pow(b, 2)), 2)
print(ans)
