cases = int(input())
for i in range(cases):
  schoolname = input()
  n_people = int(input())
  best_p = ''
  best_g = 0
  best_c = 0
  for person in range(n_people):
    inp=input()
    person = inp.split(':')[0]
    grades = inp.split(':')[1].split(',')
    total_score = 0
    total_ch = 0
    for score in grades:
      total_score += [4, 3, 2, 1][ord(score[0]) - 65] * int(score[1])
      total_ch += int(score[1])
    gpa = total_score/total_ch
    if gpa > best_g:
      best_p = person
      best_g = gpa
      best_c = total_ch
    elif gpa == best_g and total_ch > best_c:
      best_p = person
      best_g = gpa
      best_c = total_ch
  print(schoolname,"=",best_p)
  