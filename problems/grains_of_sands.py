n_input = int(input())

inputs = []
for i in range(n_input):
    n_nums = int(input())
    inputs.append([input()[::-1] for i in range(n_nums)])

for data in inputs:
    output = ''
    carry = 0
    for i in range(len(data[0])):
        total = 0
        for line in data:
            num = int(line[i])
            total += num
        total += carry
        carry = 0
        if total > 9:
            carry = int(total / 10)
            total = total % 10
        output = str(total) + output
    if carry != 0:
        output = str(carry) + output
    print(output)