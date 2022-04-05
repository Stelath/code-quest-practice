n_inp = int(input())

for i in range(n_inp):
    inp = int(input())
    if inp < 1582:
        print('No')
    elif inp % 4 != 0:
        print('No')
    elif inp % 100 != 0:
        print('Yes')
    elif inp % 400 != 0:
        print('No')
    else:
        print('Yes')
        