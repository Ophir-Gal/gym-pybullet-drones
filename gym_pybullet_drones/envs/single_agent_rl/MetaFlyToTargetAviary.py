import learn2learn
import numpy as np
from gym import spaces
from gym.utils import seeding
from learn2learn.gym.envs.meta_env import MetaEnv
import FlyToTargetAviary

class MetaFlyToTargetAviary(FlyToTargetAviary, MetaEnv):
    """
    **Description**
        Each task is defined by the location of the goal.
        The reward is proportional to the negative squared
        distance from the goal.
    """

    def __init__(self, task=None):
        self.seed()
        super(MetaFlyToTargetAviary, self).__init__(task)
        self.observation_space = self._observationSpace()
        self.action_space = self._actionSpace()
        self.reset()

    # -------- MetaEnv Methods --------
    def sample_tasks(self, num_tasks):
        """
        Tasks correspond to a goal point chosen uniformly at random.
        """
        vecs = [np.random.rand(2) for _ in range(num_tasks)]
        distance = 100.0
        unit_vecs = [distance * (vec / np.linalg.norm(vec)) for vec in vecs]
        goals = np.c_[unit_vecs, np.array([0.75] * num_tasks)]
        tasks = [{'goal': goal} for goal in goals]
        return tasks

    def set_task(self, task):
        self._task = task
        self._goal = task['goal']

    def get_task(self):
        return self._task