
f = open("cube.IGS", "r")

def global_section_parser(l):
    index = 0
    token = ""

    while l[index] != ';':
        if l[index] == ',':
            yield token.lstrip()
            index += 1
            token = ""
            continue
        else:
            if l[index] == 'H':
                index += 1
                new_index = index + int(token)
                token = l[index:new_index]
                index = new_index
                continue

        token += l[index]
        index += 1

    yield token.lstrip()


start_sec = ""
global_sec = ""
DE_sec = []
iDE = 0
for line in f:
    if line[72] == 'S':
        start_sec += line[:72]

    if line[72] == 'G':
        global_sec += line[:72]

    if line[72] == 'D':
        if iDE == 0:
            field = line.replace("\n", "")
        else:
            DE_sec.append(field + line.replace("\n", ""))
        iDE = 1 - iDE

print(start_sec)
print(global_sec)
for field in DE_sec:
    print(field)

param = []
for p in global_section_parser(global_sec):
    param.append(p)

for p in param:
    print(p)

print(len(param))