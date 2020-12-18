import numpy as np
from gym import spaces
from gym.utils import seeding
from learn2learn.gym.envs.meta_env import MetaEnv
from gym_pybullet_drones.envs.single_agent_rl.FlyToDirectionAviary import FlyToDirectionAviary

class MetaFlyToDirectionAviary(FlyToDirectionAviary, MetaEnv):
    """
    **Description**
        Each task is defined by the direction specified by _goal.
        The reward is proportional to the negative squared euclidean
        distance from the "direction location" (which is time dependent).
    """

    def __init__(self):
        super().__init__()
        self.seed()
        self.observation_space = self._observationSpace()
        self.action_space = self._actionSpace()
        self.reset()

    # -------- MetaEnv Methods --------
    def sample_tasks(self, num_tasks):
        """
        Tasks correspond to a goal point chosen uniformly at random.
        """
        goals = np.random.choice(['N','S','W','E'], size=num_tasks)
        tasks = [{'goal': goal} for goal in goals]
        return tasks

    def set_task(self, task):
        self._task = task
        self._goal = task['goal']

    def get_task(self):
        return self._task