import gym
import universe
import random


def determine_turn(turn, observations_n, j, total_sum,
                   prev_total_sum, reward_n):
    # Take average reward for 15+ iteration
    if j >= 15:
        if total_sum / j == 0:
            turn = True
        else:
            turn = False
        # reset vars
        j = 0
        prev_total_sum = total_sum
        total_sum = 0
    else:
        turn = True

    if observations_n is not None:
        j += 1
        total_sum += reward_n
    return turn, j, total_sum, prev_total_sum


def main():
    # Initialze environment
    env = gym.make('flashgames.CoasterRaces-v0')
    observations_n = env.reset()

    # init variable
    n = 0
    j = 0
    total_sum = 0
    prev_total_sum = 0
    turn = False  # action to take

    # define turn by indicating keyboard actions
    left = [('KeyEvent', 'ArrowUp', True),
            ('KeyEvent', 'ArrowLeft', True),
            ('KeyEvent', 'ArrowRight', False)]

    right = [('KeyEvent', 'ArrowUp', True),
             ('KeyEvent', 'ArrowLeft', False),
             ('KeyEvent', 'ArrowRight', True)]

    forward = [('KeyEvent', 'ArrowUp', True),
               ('KeyEvent', 'ArrowLeft', False),
               ('KeyEvent', 'ArrowRight', False)]

    # Main logic
    while True:
        n += 1
        if n > 1:
            if observations_n[0] is not None:
                prev_score = reward_n[0]

                if turn:
                    # pick a random event
                    event = random.choice([left, right])
                    action_n = [event for ob in observations_n]
                    turn = False
        elif ~turn:
            action_n = [forward for ob in observations_n]

        if observations_n[0] is not None:
            turn, j, total_sum, prev_total_sum = determine_turn(
                turn, observations_n[0], j, total_sum,
                prev_total_sum, reward_n[0]
            )

        # save new variables for each iteration
        observations_n, reward_n, done_n, info = env.step(action_n)


if __name__ == '__main__':
    main()
