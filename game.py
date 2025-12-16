"""
game.py

This file handles the core game logic for the tournament.
This file contains functions for playing individual rounds and full matches between two robots.

MATRIX REFERENCE (denote C=cooperate, denote D=defect):

C,C: (3,3)
C,D|D,C: (5,1)|(1,5)
D,D: (0,0)

author: Ryan S.
"""

#Global Variable
ROUNDS_PER_MATCH = 100

#Global Variable
PAYOFFS = {
    ("C", "C"): (3, 3),
    ("D", "C"): (5, 1),
    ("C", "D"): (1,5),
    ("D", "D"): (0, 0),
}

def play_round(robot_1, robot_2):
    """
    Returns: score_1, score_2
    """
    
    try:
        move_1 = robot_1.choose_move()
        
    except Exception as x:
        print("|ERROR| Robot 1 crashed while calling choose_move(): ", str(x))
        return
    
    try:
        move_2 = robot_2.choose_move()
        
    except Exception as y:
        print("|ERROR| Robot 2 crashed while calling choose_move(): ", str(y))
        return
    
    if move_1 not in ("C", "D"):
        print("|ERROR| Robot 1 has not chosen a valid command!")
        return
    if move_2 not in ("C", "D"):
        print("|ERROR| Robot 2 has not chosen a valid command!")
        return
    
    robot_1.record_round(move_1, move_2)
    robot_2.record_round(move_2, move_1)
    
    return PAYOFFS[(move_1, move_2)]
    
    
def play_match(robot_1, robot_2, rounds=ROUNDS_PER_MATCH):
    """
    Plays a full match (default 100 rounds) between 2 robots.
    
    returns: (score_1, score_2)
    """
    
    robot_1.reset()
    robot_2.reset()
    
    score_robot_1 = 0
    score_robot_2 = 0
    
    for i in range(rounds):
        r1 = play_round(robot_1, robot_2)
        score_robot_1 += int((r1[0]))
        score_robot_2 += int((r1[1]))
        return score_robot_1, score_robot_2
