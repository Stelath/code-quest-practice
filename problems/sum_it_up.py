n_inp = int(input())

for i in range(n_inp):
    n1, n2 = tuple([int(num) for num in input().split(' ')])
    if n1 == n2:
        print((n1 + n2) * 2)
    else:
        print(n1 + n2)