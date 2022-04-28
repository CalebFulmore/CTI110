# CTI-110
# P4HW1 - Score List
# Caleb Fulmore 
# 4/5/2022
#

# Establish a list, ask user for number of entities list will contain
ScoreList = []
UpdatedNumScores = 0
NumScores = int(input('How many scores do you want to enter? '))

# Get scores from user until the number of scores match the number user first entered
# Give error message for invalid scores, then prompt user again
# Put all scores into list
while(True):
    while(UpdatedNumScores<NumScores):
        scores = float(input('Enter score #{}: '.format(UpdatedNumScores+1)))
        while(True):
            if(scores<0 or scores>100):
                print('INVALID Score entered!!!!')
                print('Score should be between 0 and 100')
                scores = float(input('Enter score #{} again: '.format(UpdatedNumScores+1)))   
            else:
                ScoreList.append(scores)
                break
        UpdatedNumScores = UpdatedNumScores + 1 
    if(UpdatedNumScores==NumScores):
        break

# Find and remove the minimum scores
# Calculate the average and determine its letter grade
Minimum = min(ScoreList)
ScoreList.remove(min(ScoreList))
Mean = sum(ScoreList)/len(ScoreList)
if(Mean<=100 and Mean>=90 ):
    FinalGrade = 'A'
elif(Mean<=89.9 and Mean>=80):
    FinalGrade = 'B'
elif(Mean<=79.9 and Mean>=70 ):
    FinalGrade = 'C'
elif(Mean<=69.9 and Mean>=60 ):
    FinalGrade = 'D'
elif(Mean<=59.9):
    FinalGrade = 'F'

# Display results of caculations
print('-----------------Results-------------------')
print('Lowest Score  :',Minimum)
print('Modified List :',ScoreList)
print('Scores Average:',Mean)
print('Grade         :',FinalGrade)
print('-------------------------------------------')
