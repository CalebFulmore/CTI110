# Program uses functions to calculate a student's grade.
# Date
# CTI-110 P5HW1 - Score List
# Caleb Fulmore
#

##
##  Display main menu for user with choices 1, 2, and 3
##  Get user choice
##  Reject invalid user choices
##
##  Choice 1 - create score list
##  Prompt user to enter length of list
##  Get values of desired list
##  Invalid values rejected
##  Program returns to main menu
##
##  Choice 2 - display results
##  Drop lowest value
##  Display lowest value, modified list, average of list values, letter grade
##  Return to main menu
##  If no list has been created, display error
##  Returns to main menu
##
##  Choice 3
##  Terminate program
##


def MainMenu():
    print("---------------MENU--------------------")
    print("1) Create Score List")
    print("2) Display results")
    print("3) Exit")
    print("---------------------------------------")

def GetMainMenuChoice():    
    ValidChoice = False
    while ValidChoice == False:
        userChoice = input("Enter choice: ")
        if userChoice in ['1', '2', '3']:
            ValidChoice = True
        else:
            print("Invalid choice entered!!!!")
            print("Choose 1, 2, or 3 please")
            MainMenu()
            ValidChoice = False
    return userChoice

def IntCheck(number):
    try:
        number = int(number)
        return True
    except Failed:
        print("INVALID ENTRY!!")
        print("Enter a number please")
        return False
    
def createScoreList():
    scoreList = []
    validScoreCount = False
    while validScoreCount == False:    
        scoreCount = input("Enter the number of score you want to enter: ")  
        if IntCheck(scoreCount):
            scoreCount = int(scoreCount)
            if scoreCount > 0:            
                validScoreCount = True
            else:
                print("Invalid Entry.\nEnter a number greater than 0")
                validScoreCount = False
        else:
            validScoreCount = False
    
    validScore = False
    for i in range(scoreCount):
        validScore = False
        while validScore == False:
            score = input("Enter the #{} score: ".format(i+1))
            if IntCheck(score):
                score = float(score)
                if (score >=0 and score <= 100):
                    validScore = True                    
                    scoreList.append(score)
                else:
                    print("Invalid Score Entered!!!! \nPlease enter a number between 0 and 100")
                    validScore = False
            else:
                validScore = False
    return scoreList


def DisplayScoreList(scoreList):
    lowestScore = min(scoreList)
    for score in scoreList:
        if score <= lowestScore:
            lowestScore = score
    scoreList.remove(lowestScore)    
    AverageScore = sum(scoreList) / len(scoreList)
    AverageScore = round(AverageScore, 2)    
    LetterGrade = ""
    if AverageScore >= 90 and AverageScore <= 100:
        LetterGrade = "A"
    elif AverageScore >= 80 and AverageScore < 90:
        LetterGrade = "B"
    elif AverageScore >= 70 and AverageScore < 80:
        LetterGrade = "C"
    elif AverageScore >= 60 and AverageScore < 70:
        LetterGrade = "D"
    elif  AverageScore >= 0 and AverageScore <= 59:
        LetterGrade = "F"
    return scoreList, lowestScore, AverageScore, LetterGrade       
    
ModifiedScoreList = []
TerminateProgram = False            
while (TerminateProgram == False):
    MainMenu()
    choice = GetMainMenuChoice()    
    if choice == '1':        
        ModifiedScoreList = createScoreList()        
    elif choice == '2':               
        if len(ModifiedScoreList) > 0:    
            modifiedScorelist, MinimumScore, MeanScore, LetterGrade = DisplayScoreList(ModifiedScoreList)
            print('-----------------Results-------------------')
            print('Lowest Score  :',MinimumScore)
            print('Modified List :',ModifiedScoreList)
            print('Scores Average:',MeanScore)
            print('Grade         :',LetterGrade)
            print('-------------------------------------------')
        else:
            print("INVALID CHOICE!!!!")
            print("Create a list first")
    elif choice == '3':       
        print("PROGRAM TERMINATED!!!")
        print("Goodbye.")
        TerminateProgram = True
