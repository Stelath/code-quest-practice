num_in = int(input())

statuses = []
for i in range(num_in):
    statuses.append(input().split(' '))

for systems in statuses:
    error = 0
    for i, system in enumerate(systems):
        if system == 'BROKEN':
            error += [8, 4, 2, 1][i]
    
    r_led = error % 4
    l_led = int(error / 4)
    led_codes = ['off', 'red', 'green', 'blue']
    
    print(f'{led_codes[l_led]} {led_codes[r_led]}')