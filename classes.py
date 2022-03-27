from threading import Thread
import random
import time

class Player():
    #Human Player
    def __init__(self, name):
        self.name = name
        self.total = 70 #Starting at 70 for quick result

    def __str__(self):
        return f"{self.name}'s Total = {self.total}"

    def roll_the_die(self) -> int:
        Die = random.randint(1,6)
        return Die

    def play(self):
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != 'h': #Loop ends when player hit h
            print("Rolling")
            die = self.roll_the_die() #Getting die number
            print(f"Score: {die}")
            if die == 1:
                print("No score accumulated.")
                return True #Sending True to Game class for turn ending
            turn_total += die
            print(
                f"{self.name} Turn Total = {turn_total}, "
                f"{self.name} Total = {self.total}, "
                f"Possible {self.name} Total = {self.total + turn_total}"
                 )

            roll_hold = input("Roll or Hold?\n").lower()

        if roll_hold == 'h':
            self.total += turn_total
            return True #Sending True to Game class for turn ending

        print(f"{self.name} Total = {self.total}")


class ComputerPlayer(Player):
    def __init__(self, name):
        self.name = name
        self.total = 70 #Starting at 70 for quick result

    def __str__(self):
        return f"{self.name}'s Total = {self.total}"

    def play(self):
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != 'h': #Loop ends when computer decides to hold
            print("Rolling")
            die = self.roll_the_die() #Getting die number
            print(f"Score: {die}")
            if die == 1:
                print("No score accumulated.")
                return True
            turn_total += die
            print(
                f"{self.name} Turn Total = {turn_total}, "
                f"{self.name} Total = {self.total}, "
                f"Possible {self.name} Total = {self.total + turn_total}"
            )
            if turn_total >= 25:
                roll_hold = 'h'
            if self.total + turn_total >= 100:
                roll_hold = 'h'

        if roll_hold == 'h':
            self.total += turn_total
            return True #Sending True to Game class for turn ending

        print(f"{self.name} Total = {self.total}")


class PlayerFactory():
    def getPlayer(self, name, type):
        if type == 'H':
            return Player(name)
        if type == 'C':
            return ComputerPlayer(name)


class Game():
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None
        self.turn_end = False
        self.current_turn = 1
        self.win = False

    def check_winner(self,player):
        if player.total >= 100:
            self.winner = player
            return True
        else:
            return False
    
    def play_game(self):
        while not self.win: #Loop unless there is a winner
            print(f"Round {self.current_turn}\n")
            for current_player in self.players: 
                while self.turn_end == False:
                    print(current_player.name)
                    self.turn_end = True if current_player.play() == True else False #Turn ends if receives True from Player or ComputerPlayer
                    time.sleep(1) #Wait 1 sec for smoother game experience
                    print(f"\n{current_player.name} has {current_player.total}\n") 
                self.turn_end = False #Reset turn end for next player
                self.win = self.check_winner(current_player) #Sets self.win True if self.check_winner knows there is a winner
                if self.win == True:
                    break
            if self.win == True:
                break
            print("\nEnd of Turn\n\n")
            self.current_turn += 1
            

class TimedGameProxy(Game):
    def __init__(self, name1, type1, name2, type2):
        #Create factory objects for timed game
        self.player1 = PlayerFactory()
        self.player2 = PlayerFactory()
        #Sending parsed input to factory for right player creation
        self.p1 = self.player1.getPlayer(name1,type1)
        self.p2 = self.player2.getPlayer(name2,type2)
        self.timed_Game = None
        self.timer = None
        self.game = None
        self.win = False
        self.winner = None
        #Initialize timer
        self.set_timer()
        

    def count_down(self):
        self.countdownTime = 60
        while self.countdownTime > 0:
            print(self.countdownTime)
            if self.win == True: #Checks for winner every sec
                self.countdownTime = 0
                print(f"The winner is {self.winner.name}!")
                quit()
            time.sleep(1)
            self.countdownTime -= 1
        #Shows winner when time is up
        print("Time is up!")
        if self.p1.total > self.p2.total:
            print(f"The winner is {self.p1.name} with the score of {self.p1.total}")
        else:
            print(f"The winner is {self.p2.name} with the score of {self.p2.total}")
        quit()


    def timedGame(self):
        #Create Game object for timed Game
        self.timed_Game = Game(self.p1,self.p2)
        self.timed_Game.play_game() #Start game
        self.win = self.timed_Game.win #Calls if there is a winner
        self.winner = self.timed_Game.winner #Gets winner object from Game class
    

    def game_start(self):
        print("Start")
        self.timer.start() #Timer thread starts
        self.timedGame() #Calls timedGame method to start the game


    def set_timer(self): 
        print("Done setting Timer")
        self.timer = Thread(target=self.count_down)
            








