import classes
import argparse

def timed_game(p1,p2):
    #Create proxy object
    one_min_game = classes.TimedGameProxy("Player 1",p1,"Player 2",p2)
    #Starting Game
    one_min_game.game_start()

if __name__ == "__main__":
    #Parser Creation
    parser = argparse.ArgumentParser(description="Welcome to the Ultimate Game\n")
    parser.add_argument('--player1', type=str, help="Player 1: Insert H for Human player, or C for Computer",required=True)
    parser.add_argument('--player2', type=str, help="Player 2: Insert H for Human player, or C for Computer\n",required=True)
    parser.add_argument('--timed', type=str, help="Insert T for timed game",required=True)

    args = parser.parse_args()
    #Sending parsed arguments to main
    timed_game(args.player1,args.player2)
 

    