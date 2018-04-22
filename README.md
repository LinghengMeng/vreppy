# vreppy:v-rep python

**vreppy** is a python package intended to facilitate fast and convinent communication with 
[Coppelia Robotics V-REP simulator](http://www.coppeliarobotics.com/). This package is based on [reppy](https://github.com/Troxid/vrep-api-python) developed by Troxid. 

## Getting started

Install library directly from github by entering this command (If you haven't installed git, please install [git](https://gitforwindows.org/) first):

For **Mac OS**:
```bash
[sudo] pip install 'git+https://github.com/LinghengMeng/vreppy'
```
For **Windows**:
```bash
pip install git+https://github.com/LinghengMeng/vreppy
```

For **Linux**:
```bash
[sudo] pip install 'git+https://github.com/LinghengMeng/vreppy'
```

## V-Rep specific
1. Download and install [**V-Rep**](http://www.coppeliarobotics.com/downloads.html).

2. Set up environment variable for **vreppy**:

   * VREP = 'C:\Program Files\V-REP3\V-REP_PRO_EDU\'(Your V-Rep installation path)
   
   * VREP_LIBRARy = 'C:\Program Files\V-REP3\V-REP_PRO_EDU\programming\remoteApiBindings\lib\lib\Mac\' (Your V-Rep remoteApi library depending on you platform) 
  
## Test your environment
1. import vreppy


  
Package needs platform-specific native library (remoteApi). It uses two enviroment variables `VREP` and `VREP_LIBRARY`. If `VREP` is unspecified package will use default `/usr/share/vrep` for it. If `VREP_LIBRARY` is also unspecified, then it will concatenate `VREP` with `programming/remoteApiBindings/lib/lib/64Bit/`. This setup was test tested under **LINUX ONLY**. We are open for debug under Windows.
    * For windows users:
        *NOT TESTED*

To use package you will need the socket port number, which can be located in `V-REP/remoteApiConnections.txt`.

## Currently implemented things

In the current version is not implemented features such as remote management GUI,
additional configuration properties of objects and shapes, etc.
Basically implemented those components that are required to control the robot:
* Joint
* Proximity sensor
* Vision sensor
* Force sensor
* Position sensor (used for that dummy or shape object)
* ~~Remote function calls~~

## Example
Designed to be used with `examples/Pioneer.ttt`.
```python
from pyrep import VRep
import time

class PioneerP3DX:

    def __init__(self, api: VRep):
        self._api = api
        self._left_motor = api.joint.with_velocity_control("Pioneer_p3dx_leftMotor")
        self._right_motor = api.joint.with_velocity_control("Pioneer_p3dx_rightMotor")
        self._left_sensor = api.sensor.proximity("Pioneer_p3dx_ultrasonicSensor3")
        self._right_sensor = api.sensor.proximity("Pioneer_p3dx_ultrasonicSensor6")

    def rotate_right(self, speed=2.0):
        self._set_two_motor(speed, -speed)

    def rotate_left(self, speed=2.0):
        self._set_two_motor(-speed, speed)

    def move_forward(self, speed=2.0):
        self._set_two_motor(speed, speed)

    def move_backward(self, speed=2.0):
        self._set_two_motor(-speed, -speed)

    def _set_two_motor(self, left: float, right: float):
        self._left_motor.set_target_velocity(left)
        self._right_motor.set_target_velocity(right)

    def right_length(self):
        return self._right_sensor.read()[1].distance()

    def left_length(self):
        return self._left_sensor.read()[1].distance()

with VRep.connect("127.0.0.1", 19997) as api:
    r = PioneerP3DX(api)
    while True:
        rl = r.right_length()
        ll = r.left_length()
        if rl > 0.01 and rl < 10:
            r.rotate_left()
        elif ll > 0.01 and ll < 10:
            r.rotate_right()
        else:
            r.move_forward()
        time.sleep(0.1)

```


## License
Copyright (C) 2016-2017  Stanislav Eprikov, Pavel Pletenev 

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
