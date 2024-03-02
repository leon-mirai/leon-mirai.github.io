def modcalc(numerator: int, denominator: int) -> int:
    f = n // d
    return -d * f + n


n = int(input("Type numerator: "))
d = int(input("Type divisor: "))
r = modcalc(n, d)
print(r)

# r = -df + n