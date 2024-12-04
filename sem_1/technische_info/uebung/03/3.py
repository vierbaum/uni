def y1(a,b,c):
    return not ((a or b) and c)

def y2(a,b,c):
    return ((not a) and (not b)) or (not (b or c))

for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            print("%s|%s|%s|%s"%(c,b,a,y1(a,b,c)))


