from random import randint

options = ["Rock", "Paper", "Scissor"]

player_score = 0
computer_score = 0

computer = options[randint(0,2)]

player = False

while player == False:
    player = input("Rock Paper or Scissor and input exit to end game ? ")
    if player == computer:
        print("Tie")

    elif player == "Rock":
        if computer == "Paper":
            print("You Lose Computer Chose ",computer)
            computer_score = computer_score + 1
        else:
            print("You Win, Computer Chose ",computer)
            player_score = player_score + 1

    elif player == "Paper":
        if computer == "Scissor":
            print("You Lose Computer Chose ",computer)
            computer_score = computer_score + 1
        else:
            print("You Win, Computer Chose ",computer)
            player_score = player_score + 1

    elif player == "Scissor":
        if computer == "Rock":
            print("You Lose Computer Chose ",computer)
            computer_score = computer_score + 1
        else:
            print("You Win, Computer Chose ",computer)
            player_score = player_score + 1

    else:
        print("GAME END")
        print("SCORECARD")
        print("Player's Total Score = ", player_score)
        print("Computer's Total Score = ", computer_score)
        print("THANK YOU FOR PLAYING")
        exit()

    player = False
    computer = options[randint(0,2)]



