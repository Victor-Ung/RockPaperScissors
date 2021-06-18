#Rock, Paper, Scissors game

import random, sys

print("ROCK, PAPER, SCISSORS")

wins = 0
ties = 0
losses = 0

#game loop
while True:
    print("{} wins {} ties {} losses".format(wins, ties, losses))
    
    #choice loop
    while True:
        Player= input(("Please choose Rock, Paper, or Scissors (or Quit): "))
        Player = Player.lower()
        
        if Player == "quits" or Player == "q":
            sys.exit()
        
        if Player == "rock" or Player == "r" or Player == "paper" or Player == "p" or Player == "scissors" or Player == "s":
            break
        
        print('Please pick "(r)ock", "(p)aper", or "(s)cissors.')
                 
    if Player == "rock" or Player == "r":
        Player == "rock"
        print("Rock versus ...")
    if Player == "paper" or Player == "p":
        Player == "paper"
        print("Paper versus...")
    if Player == "scissors" or Player == "s":
        Player == "scissors"
        print("Scissors versus...")

    #enemyPlayer 
    enemyPlayer = random.randint(1,3)
    if enemyPlayer == 1:
        enemyPlayer = "Rock"
    if enemyPlayer == 2:
        enemyPlayer = "Paper"
    if enemyPlayer == 3:
        enemyPlayer = "Scissors"
    print(enemyPlayer)
    enemyPlayer = enemyPlayer.lower()
    
    #outcome 
    if enemyPlayer == Player:
        print("It was a tie! {} matches {}.\n".format(Player.capitalize() , enemyPlayer.capitalize()))
        ties += 1
    if enemyPlayer == "rock" and Player == "paper":
        print("It was a win! {} beats {}.\n".format(Player.capitalize(), enemyPlayer.capitalize()))
        wins += 1
    if enemyPlayer == "rock" and Player == "scissors":
        print("It was a loss! {} loses to {}.\n".format(Player.capitalize(), enemyPlayer.capitalize()))
        losses += 1
    if enemyPlayer == "paper" and Player == "rock":
        print("It was a loss! {} loses to {}.\n".format(Player.capitalize(), enemyPlayer.capitalize()))
        losses += 1
    if enemyPlayer == "paper" and Player == "scissors":
        print("It was a win! {} beats {}.\n".format(Player.capitalize(), enemyPlayer.capitalize()))
        wins += 1
    if enemyPlayer == "scissors" and Player == "rock":
        print("It was a win! {} beats {}.\n".format(Player.capitalize(), enemyPlayer.capitalize()))
        wins += 1
    if enemyPlayer == "scissors" and Player == "paper":
        print("It was a loss! {} loses to {}.\n".format(Player.capitalize(), enemyPlayer.capitalize()))
        losses += 1


        
        
    
        
        
    
    


