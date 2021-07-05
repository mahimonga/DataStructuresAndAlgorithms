n = int(input())
if n <= 1:
    print(n)
def LastDigitFibo(n):
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        c = c % 10
        b, a = c, b
    print(c)

LastDigitFibo(n)