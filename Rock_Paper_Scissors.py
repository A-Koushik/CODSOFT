import random
print("GAME INSTRUCTIONS",end="\n")
print("Rock beats scissors, scissors beat paper, and paper beats rock.",end="\n")
game=["ROCK","PAPER","SCISSORS"]
play_again=True
tol_games=0
game_history=[]
while play_again:
    n = int(input("Enter no.of games : "))
    user_score = 0
    computer_score = 0
    for i in range(n) :
        user_choice=input("Enter your choice : ")
        computer_choice=random.choice(game)
        print("Computer's choice : ",computer_choice)
        if user_choice.upper()=="ROCK" and computer_choice=="SCISSORS":
            user_score+=1
        elif user_choice.upper()=="SCISSORS" and computer_choice=="PAPER":
            user_score+=1
        elif user_choice.upper()=="PAPER" and computer_choice=="ROCK":
            user_score+=1
        elif user_choice.upper()==computer_choice :
            continue
        else :
            computer_score+=1
    print("User's score : ",user_score)
    print("Computer's choice : ",computer_score)
    if computer_score>user_score :
        print("Computer won the match.")
        game_history.append("COMPUTER")
    elif computer_score<user_score:
        print("User won the game.")
        game_history.append("USER")
    else :
        print("Draw")
        game_history.append("DRAW")
    if i==n-1:
        play=input("Do you wanna play again(yes/no) : ")
        if play.upper()=="YES" :
            play_again=True
        else :
            play_again=False
    tol_games+=1
print("Total no.of games : ",tol_games)
count_user=game_history.count("USER")
print(f"User won {count_user} times")
count_computer=game_history.count("COMPUTER")
print(f"Computer won {count_computer} times")
count_draw=game_history.count("DRAW")
print(f"Total draw matches : {count_draw}")
