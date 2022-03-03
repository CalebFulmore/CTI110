score1 = float(input("Enter score #1: "))
score2 = float(input("Enter score #2: "))
score3 = float(input("Enter score #3: "))
score4 = float(input("Enter score #4: "))
score5 = float(input("Enter score #5: "))
score6 = float(input("Enter score #6: "))
score7 = float(input("Enter score #7: "))

score_list = [score1, score2, score3, score4, score5, score6, score7]

print('-------------Results-----------')
print('Lowest Score' '  '':',min(score_list))
score_list.remove(min(score_list))
print('Modified List' ' ' ':',score_list)
num_of_scores = len(score_list)
sum_of_scores = sum(score_list)
avg_score = sum_of_scores / num_of_scores
print(f'Scores Average: {avg_score:.2f}')
print('--------------------------------')
