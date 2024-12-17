import re

def combo(operand, a, b, c):
    if operand < 4: return operand
    return [a, b, c][operand-4]

def exec_one(a, b, c):
    out = None
    for opcode, operand in zip(instr[::2], instr[1::2]):
        if opcode == 0: a = a >> combo(operand, a, b, c)
        if opcode == 6: b = a >> combo(operand, a, b, c)
        if opcode == 7: c = a >> combo(operand, a, b, c)
        if opcode == 1: b = b ^ operand
        if opcode == 2: b = combo(operand, a, b, c) & 7
        if opcode == 4: b = b ^ c
        if opcode == 5: out = combo(operand, a, b, c) & 7
    return (out, a)

a, b, c, *instr = map(int, re.findall(r"\d+", open(0).read()))

res = []
while a:
    opcode, a = exec_one(a, 0, 0)
    res.append(opcode)
print(*res, sep=',')

target = instr[::-1]

def go(a, idx):
    if idx == len(target): return a
    for check_a in range(8):
        check_a = a << 3 | check_a
        out, _ = exec_one(check_a, 0, 0)
        if out == target[idx]:
            res = go(check_a, idx+1)
            if res is not None: return res

print(go(0, 0))