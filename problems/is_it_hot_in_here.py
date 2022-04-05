n_inputs = int(input())

data = []
for inp in range(n_inputs):
    n_input_2 = int(input())
    for inp2 in range(n_input_2):
        data.append(input().split(' '))

for temp in data:
    if temp[1] == 'C':
        new_temp = float(temp[0]) * (9/5) + 32
    else:
        new_temp = (float(temp[0]) - 32) * (5/9)
    new_var = 'F' if temp[1] == 'C' else 'C'
    print(f'{temp[0]} {temp[1]} = {round(new_temp, 1)} {new_var}')
