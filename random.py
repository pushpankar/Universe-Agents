import gym
import universe

env = gym.make('flashgames.DuskDrive-v0')
env.configure(remotes=1)
observations_n = env.reset()

while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)]
                for ob in observations_n]
    observations_n, reward_n, done_n, info = env.step(action_n)
    env.render()
