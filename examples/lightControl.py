#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:45:03 2018

@author: jack.lingheng.meng
"""

import time
from vreppy import VRep
from math import *
import numpy as np
# contextlib
# simpy
# multiprocessing cpu


with VRep.connect("127.0.0.1", 19997) as vrep:

    Omnidirectional_light = vrep.light.omnidirectional("Omnidirectional_light")
    
    for i in range(10):
        Omnidirectional_light.set_light_state(i%2)
        state, diffsePart, specularPart = Omnidirectional_light.get_light_state_and_color()
        print("light state: {}".format(state))
        time.sleep(1)
        
    
vrep.simulation.stop()

