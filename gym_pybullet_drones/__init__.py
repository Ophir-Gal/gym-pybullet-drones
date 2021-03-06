from gym.envs.registration import register

register(
    id='ctrl-aviary-v0',
    entry_point='gym_pybullet_drones.envs:CtrlAviary',
)

register(
    id='dyn-aviary-v0',
    entry_point='gym_pybullet_drones.envs:DynAviary',
)

register(
    id='vision-aviary-v0',
    entry_point='gym_pybullet_drones.envs:VisionAviary',
)




register(
    id='takeoff-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:TakeoffAviary',
)

register(
    id='hover-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:HoverAviary',
)

register(
    id='flythrugate-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:FlyThruGateAviary',
)

register(
    id='avoidobstacles-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:AvoidObstaclesAviary',
)

register(
    id='flytotarget-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:FlyToTargetAviary',
)

register(
    id='metaflytotarget-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:MetaFlyToTargetAviary',
)

register(
    id='flytodirection-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:FlyToDirectionAviary',
)

register(
    id='metaflytodirection-aviary-v0',
    entry_point='gym_pybullet_drones.envs.single_agent_rl:MetaFlyToDirectionAviary',
)



register(
    id='flock-aviary-v0',
    entry_point='gym_pybullet_drones.envs.multi_agent_rl:FlockAviary',
)

register(
    id='leaderfollower-aviary-v0',
    entry_point='gym_pybullet_drones.envs.multi_agent_rl:LeaderFollowerAviary',
)

register(
    id='meetup-aviary-v0',
    entry_point='gym_pybullet_drones.envs.multi_agent_rl:MeetupAviary',
)