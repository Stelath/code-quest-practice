n_inputs = int(input())

inputs = []
for i in range(n_inputs):
    inputs.append([int(num) for num in input().split(' ')])
    
for inp in inputs:
    total = 0
    total += inp[0] * 2
    total += inp[1] * 4
    total += inp[2] * 4
    
    print(total)