# vreppy: v-rep python

**vreppy** is a python package intended to facilitate fast and convinent communication with 
[Coppelia Robotics V-REP simulator](http://www.coppeliarobotics.com/). This package is based on [reppy](https://github.com/Troxid/vrep-api-python) developed by Troxid.

Read the documentation at [vreppy.io](http://vreppy.readthedocs.io).

## Getting started

Install library directly from github by entering this command (If you haven't installed git, please install [git](https://gitforwindows.org/) first):

```bash
pip install git+https://github.com/LinghengMeng/vreppy
```

## V-Rep specific
1. Download and install [**V-Rep**](http://www.coppeliarobotics.com/downloads.html).

2. Set up environment variables for **vreppy** according to your installation path and operating system:

* `VREP = 'C:\Program Files\V-REP3\V-REP_PRO_EDU\'` (V-Rep installation path)
   
* `VREP_LIBRARy = 'C:\Program Files\V-REP3\V-REP_PRO_EDU\programming\remoteApiBindings\lib\lib\Windows\64Bit\'` 
   (V-Rep *remoteApi* library depending on you OS) 

3. To test whether you set up environemtn variables currently, you can test with commands: </br>
   `import os`</br>
   `os.environ['VREP']`</br>
   `os.environ['VREP_LIBRARY']`</br>
   (If you are working with Anaconda on Mac OS and the VREP and VREP_LIBRARY are different from your setting, you can try to open spyder from terminal: `spyder --new-instance`.)
  
## Test your **vreppy**
1. Open scene: `vrep -> File -> open scene -> scenes\testAllComponents.ttt`
2. Run: `examples\testallcomponent.py`
3. The socket port number used in `examples\testallcomponent.py` can be found in `remoteApiConnections.txt` under your installation path of V-Rep.

## Currently implemented things

In the current version is not implemented features such as remote management GUI,
additional configuration properties of objects and shapes, etc.
Basically implemented those components that are required to control the robot:
* Joints
* Sensors
   * Proximity sensor
   * Vision sensor
   * Force sensor
   * Position sensor (used for that dummy or shape object)
* Lights
   * Omnidirectional light
   * Spot light
   * Directional light
* ~~Remote function calls~~

## Example testallcomponent.py
Designed to be used with `examples/testallcomponent.ttt`.
```python
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
```
