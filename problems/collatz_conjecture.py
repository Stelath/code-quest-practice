def conjecture(start_num):
    term = start_num
    i = 1
    while term != 1:
        if term % 2 == 0:
            term /= 2
        else:
            term = (term * 3) + 1
        i += 1

    print(f'{start_num}:{i}')

start_nums = []

for i in range(int(input())):
    start_nums.append(int(input()))

for i, num in enumerate(start_nums):
    conjecture(num)