n_inp = int(input())

for i in range(n_inp):
    inp = input().split(':')
    if float(inp[0]) == 0:
        print('SAFE')
    else:
        s = float(inp[1])/float(inp[0])
        if s <= 1:
            print('SWERVE')
        elif s <= 5:
            print('BRAKE')
        else:
            print('SAFE')