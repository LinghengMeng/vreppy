#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:08:45 2018

@author: jack.lingheng.meng
"""

import time
from vreppy import VRep
import numpy as np
import gym
from gym import spaces

# define an environment with Gym API
class LivingArchitectureEnv(gym.Env):
    def __init__(self):
        # connect vrep server
        print("Connecting vrep server...")
        self.vrep = VRep.connect("127.0.0.1", 19997)
        print("Initialize vrep objects...")
        # initialize vrep objects
        # actuators
        self.j_vel = self.vrep.joint.with_velocity_control("joint_force")
        self.j_pos = self.vrep.joint.with_position_control("joint_position")
        self.j_pas = self.vrep.joint.passive("joint_passive")
        self.j_sph = self.vrep.joint.spherical("sp_joint")
        self.j_spr = self.vrep.joint.spring("joint_spring")
        
        # sensors
        self.prox_sensor = self.vrep.sensor.proximity("Proximity_sensor")
        self.s = self.vrep.sensor.proximity("sensor")
        self.v = self.vrep.sensor.vision("vision") #This could be used in end-to-end learning
        print("Initialize action and observation space...")
        # initialize action and observation space
        self.sensors_dim = 3
        self.actuators_dim = 3
        
        self.obs_max = np.array([np.inf]*self.actuators_dim)
        self.obs_min = - np.array([np.inf]*self.actuators_dim)
        self.act_max = np.array([1.]*self.sensors_dim)
        self.act_min = - np.array([1.]*self.sensors_dim)
        
        self.observation_space = spaces.Box(self.obs_min, self.obs_max)
        self.action_space = spaces.Box(self.act_min, self.act_max)
        print("Initialization done!")
        
        self.reward = 0
        
    def _self_observe(self):
        state, position = self.prox_sensor.read()
        self.observation = np.array([position.get_x(), position.get_y(), position.get_z()])
        
    def step(self, actions):
        actions = np.clip(actions, self.act_min, self.act_max)
        # take actions
        self.j_pos.set_target_position(actions[0])
        self.j_pas.set_position(actions[1])
        self.j_sph.set_matrix(
                [0, 0, 0, 0,
                 0, 0, 0, 0,
                 actions[2], 0, 0, 0])
        # observe new state
        self._self_observe()
        # reward
        if self.observation[0] != 0:
            self.reward = 1
        else:
            self.reward = 0
        
        return self.observation, self.reward, False, {}
    
    def reset(self):
        self.vrep.simulation.stop()
        self.vrep.simulation.start()
        self._self_observe()
        return self.observation
    
    def destroy(self):
        self.vrep.close_connection()

# define a reandom agent
def random_agent():
    b = np.random.randn()   #Control joint_position
    v = np.random.randn()   #Control joint_passive
    v2 = np.random.randn()  #Control sp_joint
    action = np.array([b, v, v2])
    return action   

if __name__ == '__main__':
    env = LivingArchitectureEnv()
    env.reset()
    # trival agent   
    i = 1 
    while True:
        action = random_agent()
        observation, reward, done, info = env.step(action)
        if reward == 1:
            print("{}th action".format(i))
        i = i+1
        time.sleep(0.1)
    
    env.destroy()


        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
