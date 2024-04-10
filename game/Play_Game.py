from game import Run_Play
from game.game_state import game_state
from formations.offensive.Shotgun import Shotgun
from formations.defensive.FourThree import FourThree
from Run_Play import Run_Play
from plays.offensive.FourVerticals import FourVerticals
from plays.offensive.PARead import PARead
from plays.offensive.QuickSlants import QuickSlants
from plays.offensive.Out import Out
from plays.offensive.Chaos import Chaos
from plays.offensive.Decoy import Decoy

import pygame
import random


def start(home_team, away_team):
    initial_state = game_state(offensive_formation=Shotgun(), defensive_formation=FourThree(), line_of_scrimmage_yard=85,
                               ball_position=0, first_down_yard=75, down=1, home_score=0, away_score=0, time_remaining=400,
                               has_ball='Home', home_team=home_team, away_team=away_team)

    available_plays = [Chaos(), FourVerticals(), QuickSlants(), Out(), PARead(), Decoy()]
    current_state = initial_state
    running = True
    while running:
        # Initialize the play with the current state
        field = Run_Play(current_state, simulated_game=False)

        # Run the play and get the result
        field.run_play(random.choice(available_plays))  # Run the play

        result = field.capture_final_state()

        # Check if possession is over
        if field.possession_over:
            print("Possession over. Resetting for new possession.")
            # Reset for new possession - you can change formations, line of scrimmage, etc.
            result = game_state(offensive_formation=Shotgun(), defensive_formation=FourThree(), line_of_scrimmage_yard=85,
                                ball_position=10, first_down_yard=75, down=1, home_score=result.home_score, away_score=result.away_score,
                                time_remaining=result.time_remaining, has_ball=result.has_ball, home_team=home_team, away_team=away_team)
            print(f"{home_team.name}: {result.home_score}, {away_team.name}: {result.away_score}, Time: {result.time_remaining}")

        current_state = result
        if result.time_remaining <= 0 and result.home_score-result.away_score != 0:
            running = False
            print(f"Final Score: \nHome: {result.home_score}, Away: {result.away_score}")
        elif result.time_remaining <= 0:
            print(f"Tie Game! Heading to Overtime: \nHome: {result.home_score}, Away: {result.away_score}")
            initial_overtime_state = game_state(offensive_formation=Shotgun(), defensive_formation=FourThree(), line_of_scrimmage_yard=35,
                                                ball_position=10, first_down_yard=25, down=1, home_score=result.home_score, away_score=result.away_score,
                                                time_remaining=0, has_ball=result.has_ball, home_team=home_team, away_team=away_team, overtime=True)
            current_state = initial_overtime_state
            overtime_possessions = 0
            overtime = True
            while overtime:
                field = Run_Play(current_state)
                field.run_play(random.choice(available_plays))
                result = field.capture_final_state()
                # Check if possession is over

                if field.possession_over:
                    overtime_possessions += 1
                    print("Possession over. Resetting for new possession.")
                    # Reset for new possession - you can change formations, line of scrimmage, etc.
                    result = game_state(offensive_formation=Shotgun(), defensive_formation=FourThree(), line_of_scrimmage_yard=35,
                                        ball_position=10, first_down_yard=25, down=1, home_score=result.home_score, away_score=result.away_score,
                                        time_remaining=result.time_remaining, has_ball=result.has_ball, home_team=home_team, away_team=away_team, overtime=True)
                    print(f"Home: {result.home_score}, Away: {result.away_score}")

                current_state = result

                if overtime_possessions % 2 == 0 and result.home_score - result.away_score != 0:
                    running = False
                    overtime = False
                    print(f"Final Score: \nHome: {result.home_score}, Away: {result.away_score}")

    pygame.quit()


if __name__ == "__main__":
    start()
