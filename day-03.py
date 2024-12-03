import re

def generate(s, part):
    flag = True
    for x in re.findall(r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))", s):
        if x.startswith('do'):
            flag = "'" not in x
        else:
            if flag or part == 1:
                a, b = map(int, re.findall(r"\d+", x))
                yield a * b

s = ''.join(line.strip() for line in open(0))
print(sum(generate(s, 1)))
print(sum(generate(s, 2)))
