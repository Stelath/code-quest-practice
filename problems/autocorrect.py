def calc_ham_distance(w1, w2):
    count = 0
    for i, w1_char in enumerate(w1):
        if w1_char != w2[i]:
            count += 1
    return count
        

n_inputs = int(input())

in_data = []
for inp in range(n_inputs):
    n_in = [int(num) for num in input().split(' ')]
    in_data.append({'dict_words': [input() for i in range(n_in[0])], 'miss_words': [input() for i in range(n_in[1])]})

for data in in_data:
    dict_words = data['dict_words']
    miss_words = data['miss_words']
    
    for m_word in miss_words:
        sh_distance = 99999
        correct_word = ''
        for d_word in dict_words:
            if len(m_word) == len(d_word):
                dist = calc_ham_distance(m_word, d_word)
                if dist < sh_distance:
                    sh_distance = dist
                    correct_word = d_word
        print(correct_word)