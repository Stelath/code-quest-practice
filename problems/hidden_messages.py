n_inputs = int(input())

key = input()
lines = []
for i in range(1, n_inputs):
    lines.append(input())

for line in lines:
    output = ''
    words = line.split(' ')
    for word in words:
        for num in word.split('-'):
            output += key[int(num) - 1]
        output += ' '
    output = output[:-1]
    print(output)
