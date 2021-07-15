import random

def rps_game():
    while True:
        player_selection = input("Please input one of the following choices: rock, paper or scissors: ").lower()
        options = ["rock", "paper", "scissors"] 
        rival_selection = random.choice(options)
        # validate player input 
        if player_selection not in options:
            print("Thats not a valid input try again")
            player = input("Please input one of the following choices: rock, paper or scissors: ").lower()
        
        if player_selection == rival_selection:
            return print(f"Its a Tie! Your cow chose {rival_selection}.")

        if determine_winner(player_selection, rival_selection):
            return print(f"Yay! you won! Your cow chose {rival_selection}.")
        
        else:
            print(f"How embarrasing you lost to a cow! Your cow chose {rival_selection}.")

        try:
            repeat_game = input("Would you like to play another round (yes or no): ").lower()
            if repeat_game() != "yes":
                break
        except:
            print ("You did not enter a valid value. Please enter either yes or no.")

# determine the winner from game    
def determine_winner(player, rival):
    if (player == "rock" and rival == "scissors") or (player == "scissors" and rival == "paper") or (player == "paper" and rival == "rock"):
        return True

rps_game()