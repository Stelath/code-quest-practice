n_input = int(input())

inputs = []
for i in range(n_input):
    inputs.append(input().split(' '))

for nums in inputs:
    try:
        float(nums[0])
        try:
            if float(nums[1]) == 0:
                print('Divide By Zero')
            else:
                print(round(float(nums[0]) / float(nums[1]), 1))
        except:
            print('Invalid Divisor')
    except:
        print('Invalid Dividend')
        