import gym
from gym import error, spaces, utils
from gym.utils import seeding

class LasEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    ...
  def step(self, action)->(observation, reward, done, info):
    ...
  def reset(self)->observation:
    ...
  def render(self, mode='human', close=False):
    ...
