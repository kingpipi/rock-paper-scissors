from random import randint

#intro
print("Rock...")
print("Paper...")
print("Scissors...")

player_name = str(input("New player, choose your nickname:")).capitalize()

#Interact with user
comp_react = randint(0,2)

if comp_react == 0:
    greeting = f"Welcome {player_name} to Rock, Paper, Scissors!"
elif comp_react == 1:
    greeting = f"What a funny name {player_name} is, did your parents hate you?"
else:
    greeting = f"Alas! I've finally found a {player_name} to beat at Rock, Paper, Scissors"

print(greeting)

#Define initial variables
computer_score = 0
player_score = 0
winning_score = 3
active_game = "y"

#Actual Game start
while active_game == "y":

    while computer_score < winning_score and player_score < winning_score:

        player = input(f"{player_name} make your move:").lower()

        if player == "q" or player == "quit":
            print(f"{player_name} quit game")
            computer_score = 0 #reset scores to cancel winners
            player_score = 0
            break

        if player not in ['rock','paper','scissors']:
            print("something went wrong :|")
            computer_score = 0 #reset scores to cancel winners
            player_score = 0
            break

        rand_num = randint(0,2)

        if rand_num == 0:
            computer = "rock"
        elif rand_num == 1:
            computer = "paper"
        else:
            computer = "scissors"

        print(f"Computer plays {computer}")

        if player == computer:
            print("It's a draw!")
        elif player == "rock":
            if computer == "paper":
                print("Computer wins!")
                computer_score += 1
            else:
                print(f"{player_name} wins!")
                player_score += 1
        elif player == "paper":
            if computer == "scissors":
                print("Computer wins!")
                computer_score += 1
            else:
                print(f"{player_name} wins!")
                player_score += 1
        elif player == "scissors":
            if computer == "rock":
                print("Computer wins!")
                computer_score += 1
            else:
                print(f"{player_name} wins!")
                player_score += 1

        print(f"{player_name} score: {player_score} | Computer score: {computer_score}")

    print("Game over")
    if computer_score > player_score:
        print("Computer wins game!")
    elif player_score > computer_score:
        print(f"{player_name} wins game!")

    active_game = str(input("Do you want to play again? y/n:")).lower()

#reset scores so game can restart
    computer_score = 0
    player_score = 0

print(f"Thanks for playing {player_name}, we'll soon meet again...")
