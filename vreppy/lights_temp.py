#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:01:49 2018

@author: jack.lingheng.meng
"""

from .vrep import vrep as v
from .vrep import vrepConst as vc
from .common import NotFoundComponentError, MatchObjTypeError

class AnyLight:
    def __init__(self, id, handle):
        self._id = id
        self._handle = handle
        self._def_op_mode = v.simx_opmode_oneshot_wait

class OmnidirectinalLight:
    def __init__(self, any_light: AnyLight):
        self._any_light = any_light
        
    def set_lihgt_state(self, state):
        light_handle = self._get_object_handle(name)
        emptyBuff = bytearray()
        res,retInts,retFloats,retStrings,retBuffer = vrep.simxCallScriptFunction(self._id,
                                                                       name,
                                                                       vrep.sim_scripttype_childscript,
                                                                       'setLightStateAndColor',
                                                                       [light_handle, state],[],[],emptyBuff,
                                                                       self._def_op_mode)
        if res==vrep.simx_return_ok:
            print ('setLightStateAndColor works! ',retStrings[0]) # display the reply from V-REP (in this case, just a string)
        else:
            print ('Remote function call failed')
    
    def set_lihgt_color(self, target):
        # to do

    def get_lihgt_state_and_color(self):
        emptyBuff = bytearray()
        res,retInts,retFloats,retStrings,retBuffer=vrep.simxCallScriptFunction(self._id,
                                                                               name,
                                                                               vrep.sim_scripttype_childscript,
                                                                               'getLightStateAndColor',
                                                                               [obj_handle],[],[],emptyBuff,
                                                                               vrep.simx_opmode_blocking)
        lightState = retInts[0]
        diffusePart = [retFloats[0],retFloats[1],retFloats[2]]
        specularPart = retFloats[3],retFloats[4],retFloats[5]
        return lightState, diffusePart, specularPart

class Lights:

    def __init__(self, id):
        self._id = id
        self._def_op_mode = v.simx_opmode_oneshot_wait
    
    def omnidirectional(self, name: str) -> OmnidirectinalLight:
        handle = _get_object_handle(self, name)
        light = AnyLight(self.id, handle)
        return OmnidirectinalLight(light)
    
    def spotlight(self, name: str) -> SpotLight:
        # to do
        
    def directional(self, name: str) -> DirectionalLight:
        # todo

        
    def _get_object_handle(self, name):
        code, handle = v.simxGetObjectHandle(self._id, name, self._def_op_mode)
        if code == v.simx_return_ok:
            return handle
        else:
            return None
        