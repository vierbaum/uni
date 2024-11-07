from random import shuffle

def exp(n):
    sailors = list(range(n))
    shuffle(sailors)
    res = 0
    for i, s in enumerate(sailors):
        if i == s:
            res += 1
    print(res)
    return res

repetitions = 100000

mean = 0
prob = [0, 0, 0, 0]
for _ in range(repetitions):
    prob[exp(3)] += 1 / repetitions
    #mean += exp(3) / repetitions

print(prob, sum(prob))
