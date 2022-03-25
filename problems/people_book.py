def parse_str_arr(num_ppl, str):
    arr = []
    
    str = str[1:len(str) - 1]
    parts = str.split(',')
    
    for i in range(num_ppl):
        person = []
        for j, part in enumerate(parts):
            if j % num_ppl == i:
                person.append(part.replace('[', '').replace(']', ''))
        arr.append(person)
    
    return arr

# def alphabetical(n1, n2):
#     for char_n1 in n1:
#         for char_n2 in n2:
#             if ord(char_n1.lower()) > ord(char_n2.lower()):
#                 return True
#             elif ord(char_n1.lower()) < ord(char_n2.lower()):
#                 return False

# def alphabetical_arr(names):
#     new_names = []
#     while names != []:
#         for name in names:
#             if all([alphabetical(name, name2) for name2 in names]):
#                 new_names.append(name)
#                 names.remove(name)
#     return new_names

num_in = int(input())

output = []

for i in range(num_in):
    num_ppl = int(input())
    arr_in = input()
    
    people_order = []
    for i in range(num_ppl):
        people_order.append(input())
    
    arrs = parse_str_arr(num_ppl, arr_in)
    
    for n in people_order:
        for arr in arrs:
            if arr[0] == n:
                output.append(f'Name: {arr[0]}\nAge: {arr[1]}\nInstagram: {arr[2]}\nTwitter: {arr[3]}\nPhone: {arr[4]}\nEmail: {arr[5]}')
    
    # for arr in arrs:
    #     people.append(arr)
    
    # f_names = []
    # for arr in arrs:
    #     f_names.append(arr[0])
    
    # for n in sorted(f_names):
    #     print(n)

# f_names = []
# for arr in people:
#     f_names.append(arr[0])

# for n in sorted(f_names):
#     for arr in people:
#         if arr[0] == n:
#             print(f'Name: {arr[0]}\nAge: {arr[1]}\nInstagram: {arr[2]}\nTwitter: {arr[3]}\nPhone: {arr[4]}\nEmail: {arr[5]}')

for out in output:
    print(out)