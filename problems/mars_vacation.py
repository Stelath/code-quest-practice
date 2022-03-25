import math

num_inp = int(input())

inputs = []
for i in range(num_inp):
    inputs.append([float(num) for num in input().split(' ')])

answers = []
for num in inputs:
    a = math.sqrt(num[0]**2 + num[1]**2)
    c = math.sqrt(num[2]**2 + num[3]**2)
    b = math.sqrt((num[2] - num[0])**2 + (num[1] - num[3])**2)
    
    answers.append(math.degrees(math.acos((c**2 - a**2 - b**2) / (-2 * a * b))))

for answer in answers:
    if answer > 2:
        print('WORKING HARD')
    else:
        print('VACATION')
    