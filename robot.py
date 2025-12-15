''' Robot.py

    Name: Yu Han Lin
    Date: December 14th, 2025
    Description: This is the base class for all robots. All robots should inherit from this class
    and override the choose_move() method.
    Robots have a name, a history of their own moves, and a history of their opponent's moves.
    Robot should utilize the record_round() method to keep track of moves after each round and their opponent's moves.


'''

class Robot():
    def __init__(self):
        ## Initializes the robot with a name and empty histories.
        self.name = "RoboWarrior"
        self.history = []
        self.opponent_history = []

    def reset(self):
        ## Resets the robot's history for a new game
        self.history.clear()
        self.opponent_history.clear()

    def record_round(self, move, opponent_move):
        ## Records the moves made in a round
        self.history.append(move)
        self.opponent_history.append(opponent_move)

    def choose_move(self):
        print("If you see this message, you forgot to override choose_move(). Please override this method.")
    