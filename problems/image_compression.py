n_input = int(input())

for i in range(n_input):
    n_input2 = int(input())
    inp_arr = []
    output_arr = []
    for i in range(n_input2):
        inp_arr.append(float(input()))
    min_val = 0
    max_val = 0
    for val in inp_arr:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
    for val in inp_arr:
        output_arr.append(round(((val - min_val) / (max_val - min_val)) * 255))
    
    for out in output_arr:
        print(out)
    