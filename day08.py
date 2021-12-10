import numpy as np
from numpy.core.numeric import identity

with open("files\day08.txt") as f:
    lines = [x.strip() for x in f]

inputs = [x.split(" ") for x in [line.split(" | ")[0] for line in lines]]
inputs_count = [[len(x) for x in input] for input in inputs]
outputs = [x.split(" ") for x in [line.split(" | ")[1] for line in lines]]
outputs_count = np.array([[len(x) for x in output] for output in outputs])
mask = (outputs_count == 2) | (outputs_count == 3) |(outputs_count == 4) |(outputs_count == 7)
print("Part 1 = ", len(outputs_count[mask]))


def decypher(inputs, inputs_count, outputs):
    cypher = {}
    one = set(inputs[inputs_count.index(2)])
    cypher[1] = one
    four = set(inputs[inputs_count.index(4)])
    cypher[4] = four
    tl_mid =  four - one
    seven = set(inputs[inputs_count.index(3)])
    cypher[7] = seven
    top = seven - one
    eight = set(inputs[inputs_count.index(7)])
    cypher[8] = eight
    bl_bot = eight - one - tl_mid - top
    len_6 = [x for x in inputs if len(x) == 6]
    for item in len_6:
        if set.union(one, bl_bot, top).issubset(set(item)):
            mid = eight-set(item)
    tl = four - one - mid
    len_5 = [x for x in inputs if len(x) == 5]
    for item in len_5:
        if tl.issubset(set(item)):
            five = set(item)
            cypher[5] = five
    
    bot = five - top - one - tl_mid
    br = five - top - tl_mid - bot
    tr = one - br
    bl = bl_bot - bot
    cypher[3] = set.union(seven, mid, bot)
    cypher[2] = set.union(top, tr, mid, bl_bot)
    cypher[6] = set.union(top, tl_mid, br, bl_bot)
    cypher[9] = set.union(one, top, tl_mid, bot)
    cypher[0] = eight - mid
    str_decyphered = []
    for output in outputs:
        num = [k for k, v in cypher.items() if v == set(output)][0]
        str_decyphered.append(num)
    
    decyphered = int("".join(map(str, str_decyphered)))
    return decyphered

print("Part 2 = ", sum([decypher(inputs[i], inputs_count[i], outputs[i]) for i in range(len(inputs))]))
