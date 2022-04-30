dictionary = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","Xray","Yankee","Zulu"]

n_inp = int(input())

for i in range(n_inp):
    n_inp2 = int(input())
    output_arr = []
    for i in range(n_inp2):
        inp = input()
        output = ''
        for c in inp.lower():
            if not c == ' ':
                output += dictionary[ord(c) - 97] + '-'
            else:
                output = output[:-1]
                output += ' '
        output_arr.append(output)
    for output in output_arr:
        print(output[:-1])