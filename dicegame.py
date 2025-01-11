import random
import time

# --- ASCII Messages ----------------------------------------------------------------------------------------------------->

introMessage = """
     _    _      _                            _          _   _           ______ _            _____                      _ 
    | |  | |    | |                          | |        | | | |          |  _  (_)          |  __ \                    | |
    | |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___  | | | |_  ___ ___  | |  \/ __ _ _ __ ___   ___| |
    | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \ | | | | |/ __/ _ \ | | __ / _` | '_ ` _ \ / _ \ |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | |/ /| | (_|  __/ | |_\ \ (_| | | | | | |  __/_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| |___/ |_|\___\___|  \____/\__,_|_| |_| |_|\___(_)
                                                                                                                      
"""
p1winner = """
 ____  _                         _  __        ___           _ 
|  _ \| | __ _ _   _  ___ _ __  / | \ \      / (_)_ __  ___| |
| |_) | |/ _` | | | |/ _ \ '__| | |  \ \ /\ / /| | '_ \/ __| |
|  __/| | (_| | |_| |  __/ |    | |   \ V  V / | | | | \__ \_|
|_|   |_|\__,_|\__, |\___|_|    |_|    \_/\_/  |_|_| |_|___(_)
               |___/   
"""
p2winner = """
 ____  _                         ____   __        ___           _ 
|  _ \| | __ _ _   _  ___ _ __  |___ \  \ \      / (_)_ __  ___| |
| |_) | |/ _` | | | |/ _ \ '__|   __) |  \ \ /\ / /| | '_ \/ __| |
|  __/| | (_| | |_| |  __/ |     / __/    \ V  V / | | | | \__ \_|
|_|   |_|\__,_|\__, |\___|_|    |_____|    \_/\_/  |_|_| |_|___(_)
               |___/ 
"""
one = """
        - - - - -
        -       -
        -   o   -
        -       -
        - - - - -
                        """
two = """
        - - - - -
        - o     -
        -       -
        -     o -
        - - - - -
                       """
three = """
        - - - - -
        -     o -
        -   o   -
        - o     -
        - - - - -
                       """
four = """
        - - - - -
        - o   o -
        -       -
        - o   o -
        - - - - -
                      """
five = """
        - - - - -
        - o   o -
        -   o   -
        - o   o -
        - - - - -
                     """
six = """
        - - - - -
        - o   o -
        - o   o -
        - o   o -
        - - - - -
                     """
rules1 = "These are The Dice Game Rules: "
rules2 = "• If the total of the dice is an even number, an additional 10 points are added to their score."
rules3 = "• If the total of the dice is an odd number, 5 points are subtracted from their score."
rules4 = """• If they roll a double, they get to roll one extra die and get the number of points rolled added to
their score."""
rules5 = "• The score of a player cannot go below 0 at any point."
rules6 = "• The person with the highest score at the end of the 5 rounds wins."
rules7 = """• If both players have the same score at the end of the 5 rounds, they each roll 1 die and
whoever gets the highest score wins (this repeats until someone wins)."""

list = []
filename = "Programming_Statistics"

# --- Sub-functions ---------------------------------------------------------------------------------------------->

def Intro():
    print("\n" + introMessage + "\n")

def Rules():
    print(rules1), time.sleep(1.5)
    print(rules2), time.sleep(1.5)
    print(rules3), time.sleep(1.5)
    print(rules4), time.sleep(1.5)
    print(rules5), time.sleep(1.5)
    print(rules6), time.sleep(1.5)
    print(rules7), time.sleep(1.5)


def Roll(Name, Dice1, Dice2):
    message = input(Name + " would you like to roll your dices? If yes input Y: ")
    if message ==("Y"):
        time.sleep(0.5)
        print ("You rolled: " + Dice(Dice1) + "and " + Dice(Dice2))   


def Dice(Dice):
    match Dice:
        case 1:
            return one
        case 2:
            return two
        case 3:
            return three
        case 4:
            return four
        case 5:
            return five
        case 6:
            return six
         


def Round(p1Name, p2Name):
    print("Round\n")
    p1Dice1 = int(random.randint(1,6))
    p1Dice2 = int(random.randint(1,6))
    Roll(p1Name, p1Dice1, p1Dice2)
    
    scorep1 = p1Dice1 + p1Dice2
    print("Overall: ", scorep1)
    if p1Dice1 == p1Dice2: #Double
        print("Rolled a Double. (+Bonus Roll)")
        Dice3 = int(random.randint(1,6))
        print("You rolled a: " + Dice(Dice3))
        scorep1 = scorep1 + Dice3
    scorep1 = ScoreHandling(scorep1)   
    print(p1Name + "'s score for the round is: ", scorep1, "\n")
    list.append(int(scorep1))

    p2Dice1 = int(random.randint(1,6))
    p2Dice2 = int(random.randint(1,6))
    Roll(p2Name, p2Dice1, p2Dice2) 
    scorep2 = p2Dice1 + p2Dice2
    print("Overall: ", scorep2)
    if p2Dice1 == p2Dice2: #Double
        print("Rolled a Double. (+Bonus Roll)")
        Dice4 = int(random.randint(1,6))
        print("You rolled a: " + Dice(Dice4))
        scorep1 = scorep1 + Dice4
    scorep2 = ScoreHandling(scorep2) 
    print(p2Name + "'s score for the round is: ", scorep2, "\n")
    list.append(int(scorep2))


def ScoreHandling(Score):
    if Score % 2 == 0: #Even
        print("Even score (+10)")
        Score += 10
    else:              #Odd
        print("Odd score (-5)")
        Score -= 5
    if Score < 0:
        Score = 0
    return Score    


def Decider(p1Name, p2Name):
    decider1 = random.randint(1, 6)
    decider2 = random.randint(1, 6)
    playeronedecider = input(p1Name, "would you like to roll your deciding dice? If yes input Y: ")
    if playeronedecider == ("Y"):
        print("You rolled a: " + Dice(decider1))
    playertwodecider = input("\n", p2Name, "would you like to roll your deciding dice? If yes input Y: ")
    if playertwodecider == ("Y"):
        print("You rolled a: " + Dice(decider2))
    
    p1win = decider1 - decider2
    p2win = decider2 - decider1
    if decider1 == decider2:
        print("Draw! Decider to be repeated!")
        Decider()
    elif decider1 > decider2:
        print(p1winner, "\n")
        print(p1Name, "Wins the game by: ", p1win, "points")
    elif decider2 > decider1:
        print(p2winner, "\n")
        print(p2Name, "Wins the game by: ", p2win, "points")


def Total(p1Name, p2Name):
    playeronetotal = list[0] + list[2] + list[4] + list[6] + list[8]
    playertwototal = list[1] + list[3] + list[5] + list[7] + list[9]
    time.sleep(2)
    print(p1Name, "got a total of", playeronetotal, "over the 5 rounds!")
    time.sleep(2)
    print(p2Name, "got a total of", playertwototal, "over the 5 rounds!")
    
    file = open(filename, 'a')
    file.write(p1Name + " - " + str(playeronetotal) + " " + p2Name + " - " + str(playertwototal) + "\n")
    file.close()

    if playeronetotal == playertwototal:
      print("\n" + p1Name, "and", p2Name, "got the same score!")
      print("It will go down to a decider! \n")
      Decider()
    elif playeronetotal > playertwototal:
      print(p1Name, "wins by", (playeronetotal - playertwototal), "points and", p2Name, "loses")
      print(p1winner, "\n")
    elif playertwototal > playeronetotal:
      print(p2Name, "wins by", (playertwototal - playeronetotal), "points and", p1Name, "loses")
      print(p2winner, "\n")


def Stats():
    statistics = input(str("Would you like to see all of the past scores when playing this game? If yes input Y: "))
    if statistics == ("Y"):
        file2 = open(filename, 'r')
        for line in file2:
          print("\n"+ line)


# --- Running the Code --------------------------------------------------------------------------------------------------->

Intro()
rulesquestion = input(str("Would you like to know the rules? If yes input Y: "))
if rulesquestion ==("Y"):
    Rules()
p1Name = input("\nPlayer 1. Please enter your name: ")
p2Name = input("Player 2. Please enter your name: ")
print("\n", p1Name, "VS", p2Name, "\n") 
   
def Game(p1Name, p2Name):
    i = 0
    while i < 5:
        Round(p1Name, p2Name)
        i += 1
    Total(p1Name, p2Name)
    Stats()
    playAgain = input("\nWould you like to play again? (Enter Y): ")
    if playAgain == "Y":
        Game(p1Name, p2Name)

Game(p1Name, p2Name)