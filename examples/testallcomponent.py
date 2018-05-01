import time
from vreppy import VRep
from math import *
# contextlib
# simpy
# multiprocessing cpu


with VRep.connect("127.0.0.1", 19997) as vrep:
#    vrep.simulation.stop()
#    time.sleep(2)
#vrep.simulation.start()

    j_vel = vrep.joint.with_velocity_control("joint_force")
    j_pos = vrep.joint.with_position_control("joint_position")
    j_pas = vrep.joint.passive("joint_passive")
    j_sph = vrep.joint.spherical("sp_joint")
    j_spr = vrep.joint.spring("joint_spring")
    prox_sensor = vrep.sensor.proximity("Proximity_sensor")

    s = vrep.sensor.proximity("sensor")
    v = vrep.sensor.vision("vision")

    j_vel.set_target_velocity(1)
    j_spr.set_target_position(2)
    
    print("Control joint_position...")
    for i in range(5):
        b = pi / 9
        j_pos.set_target_position(b * i + 0.2)
        time.sleep(1)
        
    print("Control joint_passive...")
    for i in range(50):
        v = sin(i / 10)
        j_pas.set_position(v)
        time.sleep(0.1)

    print("Control sp_joint...")
    for i in range(1000):
        v = sin(i / 100) * (i / 1000)
        j_sph.set_matrix(
            [0, 0, 0, 0,
             0, 0, 0, 0,
             v, 0, 0, 0])
        time.sleep(0.01)
    
    print("Read Proximity Sensor...")
    while True:
        state, position = prox_sensor.read()
        if position.get_x() != 0:
            print("Detect something!")
        else:
            print("Nothing!")
        #print("position:{}".format(position.distance()))

#vrep.simulation.stop()

