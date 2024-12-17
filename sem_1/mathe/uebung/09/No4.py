class num:
    def __init__(self, value):
        self.value = value

    def __add__(self, o):
        return num((self.value + o.value) % 6)

    def __mul__(self, o):
        return num((self.value * o.value) % 6)

    def __repr__(self):
        return str(self.value)

class Vec:
    def __init__(self, values):
        self.values = values

        if isinstance (self.values, num):
            self.values = [self.values]

        for i, v in enumerate(self.values):
            if not isinstance(v, num):
                self.values[i] = num(v)

    def __repr__(self):
        return str(self.values)

    def __mul__(self, o):
        print(self, o)
        if len(self.values) != len(o.values):
            raise ValueError("vector product wrong dimensions")

        res = num(0)
        for i, j in zip(self.values, o.values):
            res += i * j

        return res

class Matrix:
    def __init__(self, values):
        self.hvalues = [Vec(v) for v in values]
        self.vvalues = []

        for i in range(len(values[0])):
            self.vvalues.append(Vec([values[j][i] for j in range(len(values))]))

        print("VV", self.vvalues)
        print("HV", self.hvalues)

        self.size = (len(self.vvalues), len(self.hvalues))

    def __repr__(self):
        res = "[\n"
        for v in self.hvalues:
            res += "\t" + str(v) + "\n"

        return res + "]"

    def __mul__(self, o):
        print(o.vvalues)
        if not isinstance(o, Matrix):
            raise ValueError("matrix can only be multiplied by matrix")

        res = []

        for i, v in enumerate(self.hvalues):
            row = []
            for j in range(o.size[0]):
                row.append(v * o.vvalues[j])
            res.append(row)
        return Matrix(res)

a = Matrix([
    [4,0,0,4,5],
    [5,5,0,2,2]
])

b = Matrix([
    [5,2],
    [3,0],
    [3,4],
    [4,0],
    [1,0]
])

print(b*a)