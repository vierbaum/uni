def gcd(a, b, depth=0, q = []):
    if b > a:
        b, a = a, b

    factor = a // b
    offset = a - b * factor

    if offset > 0:
        print("r_%s = %s= %s\\cdot %s + %s"%(depth, a, factor, b, offset))
        gcd(b, offset, depth + 1, q + [factor])
    else:
        print("r_%s = %s= %s\\cdot %s + %s"%(depth, a, factor, b, offset))
        return



gcd(29, 17)
print()
gcd(713, 552)
print()
gcd(11253, 2607)
