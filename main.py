n = int(input("Enter the n value: "))
s = []
a, b = 0, 1
for _ in range(n+1):
    s.append(a)
    a, b = b, a + b
print(s)