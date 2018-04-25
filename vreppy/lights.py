#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:08:30 2018

@author: jack.lingheng.meng
"""

from .vrep import vrep as v
from .vrep import vrepConst as vc
from .common import NotFoundComponentError, MatchObjTypeError

class AnyLight:
    def __init__(self, id, handle, name):
        self._id = id
        self._handle = handle
        self._name = name
        self._def_op_mode = v.simx_opmode_oneshot_wait
        
    def set_light_state(self, state):
        #if current state == target state then do nothing
        lightState, diffusePart, specularPart = self.get_light_state_and_color()
        if lightState == state:
            print("you are at what you want")    
        else:
            emptyBuff = bytearray()
            res,retInts,retFloats,retStrings,retBuffer = v.simxCallScriptFunction(self._id,
                                                                           self._name,
                                                                           v.sim_scripttype_childscript,
                                                                           'setLightStateAndColor',
                                                                           [self._handle, state],[],[],emptyBuff,
                                                                           self._def_op_mode)
            if res==v.simx_return_ok:
                print ('setLightStateAndColor works! ',retStrings[0]) # display the reply from V-REP (in this case, just a string)
            else:
                print ('Remote function call failed')
    
#    def set_lihgt_color(self, target):
#        # to do


    def get_light_state_and_color(self):
        emptyBuff = bytearray()
        res,retInts,retFloats,retStrings,retBuffer=v.simxCallScriptFunction(self._id,
                                                                               self._name,
                                                                               v.sim_scripttype_childscript,
                                                                               'getLightStateAndColor',
                                                                               [self._handle],[],[],emptyBuff,
                                                                               v.simx_opmode_blocking)
        if res==v.simx_return_ok:
            print ('getLightStateAndColor works! ',retStrings[0]) # display the reply from V-REP (in this case, just a string)
        else:
            print ('Remote function call failed: getLightStateAndColor')
        lightState = retInts[0]
        diffusePart = [retFloats[0],retFloats[1],retFloats[2]]
        specularPart = retFloats[3],retFloats[4],retFloats[5]
        return lightState, diffusePart, specularPart

class OmnidirectinalLight:
    def __init__(self, any_light: AnyLight):
        self._any_light = any_light
        
    def set_light_state(self, state):
        return self._any_light.set_light_state(state)
    
    def get_light_state_and_color(self):
        return self._any_light.get_lihgt_state_and_color()
        
class SpotLight:
    def __init__(self, any_light: AnyLight):
        self._any_light = any_light
        
    def set_light_state(self, state):
        return self._any_light.set_light_state(state)
    
    def get_light_state_and_color(self):
        return self._any_light.get_lihgt_state_and_color()
     
class DirectionalLight:
    def __init__(self, any_light: AnyLight):
        self._any_light = any_light
        
    def set_light_state(self, state):
        return self._any_light.set_light_state(state)
    
    def get_light_state_and_color(self):
        return self._any_light.get_lihgt_state_and_color()

class Lights:

    def __init__(self, id):
        self._id = id
        self._def_op_mode = v.simx_opmode_oneshot_wait
    
    def omnidirectional(self, name: str) -> OmnidirectinalLight:
        handle = self._get_object_handle(name)
        light = AnyLight(self._id, handle, name)
        return OmnidirectinalLight(light)
    
    def spotlight(self, name: str) -> SpotLight:
        handle = self._get_object_handle(name)
        light = AnyLight(self._id, handle, name)
        return SpotLight(light)
    

    def directional(self, name: str) -> DirectionalLight:
        handle = self._get_object_handle(name)
        light = AnyLight(self._id, handle, name)
        return DirectionalLight(light)
        
    def _get_object_handle(self, name):
        code, handle = v.simxGetObjectHandle(self._id, name, self._def_op_mode)
        if code == v.simx_return_ok:
            return handle
        else:
            raise NotFoundComponentError("Handle not found")
            return None
        