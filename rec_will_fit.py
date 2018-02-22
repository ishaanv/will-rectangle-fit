import math

a, b = map(lambda x: float(x) / 2,
           input('enter dimensions of larger rec: ').split(' '))
c, d = map(lambda x: float(x) / 2,
           input('enter dimensions of smaller rec: ').split(' '))
f = math.hypot(c, d)
p = b - math.sqrt(math.pow(f, 2) - math.pow(a, 2))
q = a - math.sqrt(math.pow(f, 2) - math.pow(b, 2))

ans = p > 0 and q > 0 and math.pow(2 * d, 2) <= math.pow(p, 2) + math.pow(q, 2)
print(ans)
