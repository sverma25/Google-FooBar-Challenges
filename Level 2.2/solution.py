def answer(pegs):
    peg_dist = [(pegs[i+1] - pegs[i]) for i in range(len(pegs) - 1)]
    diff = sum(peg_dist[::2]) - sum(peg_dist[1::2])

    radius_gear1 = 0
    if len(peg_dist)%2 == 0:
        if diff < 1: return [-1,-1]

        radius_gear1 = [2*diff, 1]
    else:
        if diff < 3: return [-1,-1]

        if diff%3 == 0: radius_gear1 = [int(2*diff/3), 1]
        else: radius_gear1 = [2*diff, 3]

    return validate(peg_dist, radius_gear1)

def validate(peg_dist, radius_gear1):
    start = radius_gear1[0]/radius_gear1[1]

    for i in range(0,len(peg_dist)):
        if peg_dist[i] - start < 1: return [-1, -1]
        start = peg_dist[i] - start

    return radius_gear1

# print(answer([1,14,21,30]))
