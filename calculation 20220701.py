n = int(input('Please input n: '))

s = 1.0

for i in range(2, n+1):
    s = s + 1 / i*(-1)**i

print(s)