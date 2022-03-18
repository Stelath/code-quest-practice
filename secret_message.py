input()
num_lines = int(input())
text = input()
origin = input().split(',')
lines_covered = int(input())
cover = input()

line_len = int(len(text) / num_lines)
print(line_len)
message_arr = [[''] * line_len] * num_lines
for i, character in enumerate(text):
    line_num = int(i / line_len)
    message_arr[line_num][i - (line_num * line_len)] = character

cover_len = int(len(cover) / lines_covered)
cover_arr = [[''] * cover_len] * lines_covered
for i, character in enumerate(text):
    line_num = int(i / cover_len)
    cover_arr[line_num][i - (line_num * line_len)] = character

message_arr = message_arr[origin[0]:][origin[1]:]

decode = ''
for i, m_char_arr in enumerate(message_arr):
    for j, m_char in enumerate(m_char_arr):
        if m_char == cover_arr[i][j]:
            decode += m_char
            
print(decode)