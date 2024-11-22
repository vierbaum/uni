def gamma(p, s):
    if p == "p_0":
        if s == a:
            return "p_1"
        return "p_f"

    if p == "p_1":
        if s == a:
            return "p_2"
        return "p_f"
    if p == "p_2":
        if s == a:
            return "p_0"
        return "p_f"

    return  "p_f"

def delta(p, s):
    if p == "q_0":
        return "q_1"

    return "q_0"

A = dict()
A["P"] = ["p_0", "p_1", "p_2", "p_f"]
A["Sigma"] = "ab"
A["gamma"] = gamma
A["p_0"] = "p_0"
A["E"] = ["p_0", "p_1"]

B = dict()
B["Q"] = ["q_0", "q_1"]
B["Sigma"] = "ab"
B["delta"] = delta
B["p_0"] = "q_0"
B["E"] = ["q_0"]

for p in A["P"]:
    for q in B["Q"]:
        for a in A["Sigma"]:
            print("((%s,%s),%s)\\mapsto (%s,%s)"%(p,q,a, A["gamma"](p, a), B["delta"](q, a)))
