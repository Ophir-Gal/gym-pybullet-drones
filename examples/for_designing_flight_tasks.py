import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
print("YAY")

p.loadURDF(r"..\gym_pybullet_drones\assets\cf2x.urdf",
                           [0, 0.5, .75],
                           p.getQuaternionFromEuler([0, 0, 0]),
                           physicsClientId=physicsClient
                           )

for i in [0,1,-1]:
    for j in range(30):
        p.loadURDF(r"..\gym_pybullet_drones\assets\architrave.urdf",
                           [i, 2+2*abs(-i), j*.06],
                           p.getQuaternionFromEuler([0, 0, 0]),
                           physicsClientId=physicsClient
                           )

