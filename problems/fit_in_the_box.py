n_inputs = int(input())

for i in range(n_inputs):
    inp = [int(inp) for inp in input().split(' ')]
    text = input()
    output_arr = []
    output = ''
    for word in text.split(' '):
        if len(output) + len(word) <= inp[0]:
            output += word + ' '
        else:
            output_arr.append(output[:-1])
            output = word + ' '
    output_arr.append(output[:-1])
    
    if len(output_arr) <= inp[1]:
        for output_arr_case in output_arr:
            print(output_arr_case)
    else:
        print('WILL NOT FIT')