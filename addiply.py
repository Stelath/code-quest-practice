num_in = int(input())

nums = []
for i in range(num_in):
    nums.append([int(num) for num in input().split(' ')])

for arr in nums:
    p_num = arr[0] + arr[1]
    m_num = arr[0] * arr[1]
    
    print(f'{p_num} {m_num}')