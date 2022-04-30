# for x in range(int(input())):
#     c, r = 20, 20
#     screen = [[10 for x in range(c)] for y in range(r)]
#     row, column = map(int, input().split())
#     screen[row][column] = 100
#     print(screen)

def distance(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    count = 0
    while x1 != x2 or y1 != y2:
        if x1 > x2:
            x1 -= 1
        elif x1 < x2:
            x1 += 1
        if y1 > y2:
            y1 -= 1
        elif y1 < y2:
            y1 += 1
        count += 1
    return count

n_inp = int(input())
for i in range(n_inp):
    inp = [int(coord) for coord in input().split(' ')]
    output = []
    for i in range(20):
        smaller_arr = []
        for j in range(20):
            dist = distance((inp[1], inp[0]), (j, i))
            smaller_arr.append([100, 50, 25, 10][dist if dist < 3 else 3])
        output.append(smaller_arr)
    for i in output:
        print(str(i).replace(',', '').replace('[', '').replace(']', ''))