n_input = int(input())

inputs = []
for i in range(n_input):
    inputs.append([int(num) for num in input().split(' ')])

for data in inputs:
    loop = True
    length = 0
    while loop:
        if length == data[2]:
            print('true')
            loop = False
        elif data[1] > 0 and (5 + length) <= data[2]:
            length += 5
            data[1] -= 1
        elif data[0] > 0 and (1 + length) <= data[2]:
            length += 1
            data[0] -= 1
        else:
            print('false')
            loop = False
