#Author: Noah Colaco
#Date: Tuesday, May 2, 2017
#File Name: rock_paper_scissors.py
#Description: 


from easygui import * #Import easGUI
import random #Import the built in random library from Python

def helpMessage(): #Make 'helpMessage()' a function that displays how to play the game of rock paper scissors.
    msgbox(msg='You are going to play a game of rock paper scissors against the computer. There will be a choice for you to choose rock paper or scissors and the computer will randomly choose rock paper or scissors. Each game goes to best of 3 rounds, whoever gets to 2 wins first wins the game. Press "OK" to continue.', title='How to Play', ok_button='OK', image=None) #Display a message box telling the user how to play the game.

def userName(): #Make 'userName()' a function that gets the user's name.
    user_name = enterbox(msg='Enter Your Name: ', title='UserName', default='') #Make an enter box appear so the user can input their name.
    return user_name #Return 'user_name' back to the variable it is being used in.

def programInput(): #Make a function called 'programInput' that gets an input from the user for if they want to start or quit the program, or if they want the help menu.
    choice = buttonbox(msg = 'What would you like to do?', choices = ['Start', 'Help', 'Quit']) #Make a button box appear asking the user if they want to start, quit, or display the help menu, and store their choice in the variable 'choice'.
    return choice #Return 'choice' back to the variable it is being used in.

def programChoice(choice, flag): #Make 'programChoice()' a function that decides what the user wants to do.
    if choice == 'Start': #Check if 'choice' is 'Start'.
        flag = True #Make 'flag' True.
    elif choice == 'Help': #Check if 'choice' is 'Help'.
        helpMessage() #Display the help messagebox using the 'helpmessage()' function.
        choice = programInput() #Make 'choice' hold the decision of the function 'programInput()'
        flag = programChoice(choice, flag) #Make 'flag' hold the decision of the function programChoice().
    elif choice == 'Quit': #Check if 'choice' is 'Quit'.
        flag = False #Make 'flag' False.
    else: #Check if everythhing else in the 'if' statement is False.
        print('This should not happen #1') #Display a message saying this should not happne #1.
    return flag #Return 'flag' back to the variable it is being used in. 

def askUser(): #Make 'askUser()' a function that asks the user to pick rock paper or scissors.
    msg = 'Pick One' #Make 'msg' display 'Pick One'.
    choices = ['Rock', 'Paper', 'Scissors'] #Make the choices the user has to pick: Rock, Paper or Scissors.
    user_choice = buttonbox(msg, choices=choices) #Ask the user to pick rock paper or scissors and store their choice in the variable 'user_choice'.
    return user_choice #Rreturn 'user_choice' back to the variable it is being used in.

def computerChoice(): #Make 'computerChoice()' a function that randomly chooses Rock Paper or Scissors.
    computer_choice = random.randint(1,3) #Make 'computer_choice' equal a random integer between 1 and 3 inclusive.
    if computer_choice == 1: #Check if 'computer_choice' is equal to 1.
        computer_choice = 'Rock' #Make 'computer_choice' equal to 'Rock'.
    elif computer_choice == 2: #Check if 'computer_choice' is equal to 2.
        computer_choice = 'Paper' #Make 'computer_choice' equal to 'Paper'.
    elif computer_choice == 3: #Check if 'computer_choice' is equal to 3.
        computer_choice = 'Scissors' #Make 'computer_choice' equal to 'Scissors'.
    else: #Check if everything else in the 'if' statement is False.
        print('This should not happen #2') #Display a message saying 'This should not happen #2'.
    return computer_choice #Return 'computer_choice' back to the variable it is being used in.

def showComputerChoice(computer_choice): #Make 'showComputerChoice()' a function that shows what the computer chose.
    if computer_choice == 'Rock': #Check if 'computer_choice' is Rock.
        image = './Rock.gif' #Make 'image' equal Rock.gif
    elif computer_choice == 'Paper': #Check if 'computer_choice' is Paper.
        image = './Paper.gif' #Make 'image' equal Paper.gif
    elif computer_choice == 'Scissors': #Check if 'computer_choice' is Scissors.
        image = './Scissors.gif' #Make 'image' equal Scissors.gif
    else: #Check if everything else in the 'if' statement is False.
        print('This should not happen #3') #Display a message saying 'This should not happen #3'.
    msgbox(msg='The Computer Chose ' + computer_choice, title='The Computer Choice', ok_button='OK', image=image) #Display what the computer choice was in the form of a message box.

def showUserChoice(user_choice, user_name):
    if user_choice == 'Rock': #Check if 'user_choice' is Rock.
        image = './Rock.gif' #Make 'image' equal Rock.gif
    elif user_choice == 'Paper': #Check if 'user_choice' is Paper.
        image = './Paper.gif' #Make 'image' equal Paper.gif
    elif user_choice == 'Scissors': #Check if 'user_choice' is Scissors.
        image = './Scissors.gif' #Make 'image' equal Scissors.gif
    else: #Check if everything else in the 'if' statement is False.
        print('This should not happen #4') #Display a message saying 'This should not happen #4'.
    msgbox(msg= 'You Chose ' + user_choice, title= user_name + ' Choice', ok_button='OK', image=image) #Display what the user choice was in the form of a message box.

def computerScoreDecider(user_choice, computer_choice, computer_score): #Make 'computerScoreDecider()' a function that checks if the computer won the round and if the computer won give it a point.
    if user_choice == 'Rock': #Check if 'user_choice' is Rock.
        if computer_choice == 'Paper': #Check if 'computer_choice' is Paper.
            computer_score = computer_score + 1 #Add 1 to the computer's score to indicate they won a round.
        else: #Check if the 'if' statement is False.
            nothing = True #Make 'nothing' equal True so that nothing happens.
    elif user_choice == 'Paper': #Check if 'user_choice' is Paper.
        if computer_choice == 'Scissors': #Check if 'computer_choice' is Scissors.
            computer_score = computer_score + 1 #Add 1 to the computer's score to indicate they won a round.
        else: #Check if the 'if' statement is False.
            nothing = True #Make 'nothing' equal True so that nothing happens.
    elif user_choice == 'Scissors': #Check if 'user_choice' is Scissors.
        if computer_choice == 'Rock': #Check if 'computer_choice' is Rock.
            computer_score = computer_score + 1 #Add 1 to the computer's score to indicate they won a round.
        else: #Check if the 'if' statement is False.
            nothing = True #Make 'nothing' equal True so that nothing happens.
    else: #Check if everything else in the 'if' statement is False.
        print('This should not happen #5') #Display a message saying 'This should not happen #3'.
    return computer_score #Return 'computer_score' back to the variable it is being used in.

def userScoreDecider(user_choice, computer_choice, user_score): #Make 'userScoreDecider()' a function that checks if the user won the round and if the user won give them a point.
    if user_choice == 'Rock': #Check if 'user_choice' is Rock.
        if computer_choice == 'Rock':  #Check if 'computer_choice' is Rock.
            nothing = True #Make 'nothing' equal True so that nothing happens.
        elif computer_choice == 'Scissors': #Check if 'computer_choice' is Scissors.
            user_score = user_score + 1 #Add 1 to the user's score.
        else: #Check if everything else in the 'if' statement is False.
            nothing = True #Make 'nothing' equal True so that nothing happens.
    elif user_choice == 'Paper': #Check if 'user_choice' is Paper.
        if computer_choice == 'Rock': #Check if 'computer_choice' is Rock.
            user_score = user_score + 1 #Add 1 to the user's score.
        elif computer_choice == 'Paper': #Check if 'user_choice' is Paper.
            nothing = True #Make 'nothing' equal True so that nothing happens.
        else: #Check if everything else in the 'if' statement is False.
            nothing = True #Make 'nothing' equal True so that nothing happens.
    elif user_choice == 'Scissors': #Check if 'user_choice' is Scissors.
        if computer_choice == 'Paper': #Check if 'user_choice' is Paper.
            user_score = user_score + 1 #Add 1 to the user's score.
        elif computer_choice == 'Scissors': #Check if 'computer_choice' is Scissors.
            nothing = True #Make 'nothing' equal True so that nothing happens.
        else: #Check if everything else in the 'if' statement is False.
            nothing = True #Make 'nothing' equal True so that nothing happens.
    else: #Check if everything else in the 'if' statement is False.
        nothing = True #Make 'nothing' equal True so that nothing happens.
    return user_score #Return 'user_score' back to the variable it is being used in.


def scoreBox(user_score, computer_score, user_name): #Make 'scoreBox' a function that shows the score of you and the computer.
    msgbox(msg='Computer: ' + str(computer_score) + ' Wins' + '    ' + user_name + ': ' + str(user_score) + ' Wins', title='Score', ok_button='Continue') #Display how many rounds you and the computer won in the form of a messsage box.


def winnerDecider(user_score, computer_score, user_name): #Make 'winnderDecider()' a function that checks who won and display who won in the form of a message box.
    if user_score == 2: #Check if the user won two rounds.
        msgbox(msg='Congratulations ' + user_name + ', You Win!', title='YOU WIN', ok_button='Exit') #Tell the user they won in the form of a message box.
    elif computer_score == 2: #Check if the user won two rounds.
        msgbox(msg='Better Luck Next Time ' + user_name + ', You Lost!', title='YOU LOST', ok_button='Exit') #Tell the user they lost in the form of a message box.
    else: #Check if everything else in the 'if' statement is False.
        nothing = True #Make 'nothing' equal True so that nothing happens.


        
user_score = 0 #Make 'user_score' equal 0
computer_score = 0 #Make 'computer_score' equal 0
flag = True #Make 'flag' True.
helpMessage() #Use the 'helpMessage()' function to display a message box telling the user how to play the game.
user_name = userName() #Make 'user_name
choice = programInput()
flag = programChoice(choice, flag)
if flag == True:
    while user_score < 2 or computer_score < 2:
        if user_score == 2 or computer_score == 2:
            flag = False
        else:
            user_choice = askUser()
            showUserChoice(user_choice, user_name)
            computer_choice = computerChoice()
            showComputerChoice(computer_choice)
            user_score = userScoreDecider(user_choice, computer_choice, user_score)
            computer_score = computerScoreDecider(user_choice, computer_choice, computer_score)
            scoreBox(user_score, computer_score, user_name)
            winnerDecider(user_score, computer_score, user_name)
elif flag == False:
    flag = False
else:
    print('This should not happen #6')
