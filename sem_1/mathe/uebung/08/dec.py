import math

def div(numerator, denominator, period=[], depth=1):
    print(numerator, denominator)
    if numerator in period:
        print("\\frac{%s}{%s}"%(numerator, denominator * depth))
        return

    remainder = numerator % denominator
    dec = numerator // denominator
    print("rem %s dec %s"%(remainder, dec))

    div(remainder * 10, denominator, period + [numerator], depth * 10)
    print("\\frac{%s}{%s} + \\frac{%s}{%s}"%(dec, depth, remainder, denominator * depth))


print(div(15, 7))