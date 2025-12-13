"""
test.py

Check to test whether robots run

author: Ryan S.
"""

from robot import Robot

def test_robot(robot):
    
    if not isinstance(robot, Robot):
        raise TypeError("Robot must inherit from the base class.")
    
    required_methods = ["choose_move", "reset", "record_round"]
    for method in required_methods:
        if not hasattr(robot, method):
            raise AttributeError("Missing method: ", str(method))
        
    try:
        move = robot.choose_move()
    except Exception as j:
        raise RuntimeError("choose_move() crashed: ", str(j))
    
    if move not in ("C", "D"):
        raise ValueError("choose_move() must return option C or D")
    
    robot.reset()
    robot.record_round("C", "D")
    
    if robot.history != ["C"]:
        raise ValueError("History not recorded correctly!")
    
    print("Robot passed all basic tests")