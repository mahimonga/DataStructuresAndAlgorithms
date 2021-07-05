a, b = [int(i) for i in input().split()]

def lcm(a,b):
    if b == 0:
        return a
    c = a % b
    return lcm(b, c)

if a > b:
    final_lcm = lcm(a, b)
else:
    final_lcm = lcm(b, a)

print(a * b // final_lcm)