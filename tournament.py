import game

# Import however many robots, these are placeholders
import robot1
import robot2


def main():
    """
    Main logic
    """

    # Initialize players
    # Add player classes here (each should be a robot class)
    player_classes = [
        robot1.robot,
        robot2.robot
    ]

    # This list will store successfully created robot instances
    players = []

    # Attempt to instantiate each robot class
    # If successful, add the robot to the players list
    for robot_cls in player_classes:
        try:
            robot_instance = robot_cls()
            players.append(robot_instance)

        except Exception as e:
            # If instantiation fails, report which robot failed
            # Skip this robot and continue with the others

            print("ALERT: %s HAS FAILED TO ACTIVATE" %
                (robot_cls.__name__))
            continue

    # Run the entire tournament using the list of valid players
    scores = run_entire_tournament(players)

    # Display the final averaged results in a formatted output
    print_results(scores)


def run_entire_tournament(players):
    """
    Runs the full tournament 5 times and averages the scores.
    """

    total_scores = {}

    # Initialize total scores
    for player in players:
        total_scores[player.name] = 0

    # Run tournament 5 times
    for _ in range(5):
        tournament_scores = run_tournament(players)
        for name, score in tournament_scores.items():
            total_scores[name] += score

    # Average scores
    average_scores = {}
    for name, score in total_scores.items():
        average_scores[name] = score / 5

    return average_scores


def run_tournament(players):
    """
    Runs a single round-robin tournament.
    Each robot plays every other robot once.
    """

    scores = {}

    # Initialize scores
    for player in players:
        scores[player.name] = 0

    # Round-robin matches
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            robota = players[i]
            robotb = players[j]

            try:
                # Attempt to play the match normally
                score_a, score_b = game.play_match(robota, robotb)
                scores[robota.name] += score_a
                scores[robotb.name] += score_b

            except Exception as e:
                # If nothting is returned, check which robots are still functional
                # Default points flag
                a_works, b_works = True, True

                # Test robota
                try:
                    robota.choose_move()
                except Exception:
                    a_works = False

                # Test robotb
                try:
                    robotb.choose_move()
                except Exception:
                    b_works = False

                # Working robot automatically wins 5 points
                if a_works and not b_works:
                    scores[robota.name] += 5
                elif b_works and not a_works:
                    scores[robotb.name] += 5

                # If neither works, no points are awarded
                continue

    return scores


def print_results(scores):
    """
    Prints the tournament results in the spy theme.
    """

    # Pretty fluff
    print("\n============ MISSION REPORT ============")

    # Sort by highest score
    for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        # %-30s → left-align name in 30 spaces
        # %10.2f → right-align score in 10 spaces
        print("%-30s%10.2f" % (name, score))
        print("----------------------------------------")

    print("\n=== OFFICE OF INORGANIC INTELLIGENCE ===")

