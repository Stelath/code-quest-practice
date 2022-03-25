n_input = int(input())

inputs = []
for i in range(n_input):
    inputs.append(int(input()))

def toBinary(i, wid):
    output = ''
    while i > 0:
        output = str(i % 2) + output
        i = int(i / 2)
    return output.zfill(wid)

for num in inputs:
    for i in range(2**num):
        print(toBinary(i, num))