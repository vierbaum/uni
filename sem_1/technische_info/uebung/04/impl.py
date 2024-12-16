PARAMS = 4

def gen_prefix(x1="0", x2="0", x3="0", x4="0"):
    return x4, x3, x2, x1

def gen_value(i, minterms, dc):
        if i in minterms:
            return "1"
        elif i in dc:
            return "-"

        return "0"

def gen_table(minterms, dc):
    for i in range(2**PARAMS):
        prefix = str(bin(i)[2:])
        prefix = gen_prefix(*prefix[::-1])

        print("\t%s&%s&%s&%s&%s&%s\\\\"%(i,*prefix,gen_value(i, minterms, dc)))

def KV(minterms, dc):
    lines = ((0,1,4,5), (2,3,7,6), (10, 11, 15, 14), (8, 9, 13, 12))
    for l in lines:
        print("%s&%s&%s&%s\\\\"%(
            gen_value(l[0], minterms, dc),
            gen_value(l[1], minterms, dc),
            gen_value(l[2], minterms, dc),
            gen_value(l[3], minterms, dc)
            ))

if __name__ == "__main__":
    minterms = (0, 3, 4, 6, 10, 14, 15)
    dc = (1, 5, 7, 11)
    print("\\documentclass{article}\n\\begin{document}")
    print("\\begin{tabular}{r|cccc|l}")
    gen_table(minterms, dc)
    print("\\end{tabular}")
    print("\\begin{tabular}{c|c|c|c}")
    KV(minterms, dc)
    print("\\end{tabular}")

    minterms = (0,1,2,11,15)
    dc = ()
    print("\\begin{tabular}{r|cccc|l}")
    gen_table(minterms, dc)
    print("\\end{tabular}")
    print("\\begin{tabular}{c|c|c|c}")
    KV(minterms, dc)
    print("\\end{tabular}")
    print("\\end{document}")
