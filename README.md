# UIgnite

 A basic UI client made with Tkinter in python 2.7 for controlling engine ignition tests via XBee radios.  
 Built to work with the Arduino server.
![screen shot 2017-10-25 at 10 24 07 am](https://user-images.githubusercontent.com/20449016/32208520-664bc2a6-bdd9-11e7-882c-718dc20fb6dc.png)

## Python Client
### Running
To run, make sure your system satisfies requirements.txt and that you are running python 2.7

If you're not running python 2.7 and/or don't want to run python 2.7, you could always change `Tkinter` to `tkinter` in the import statement of `application.py` and it would probably work.

`application.py` takes 2 arguments in order to run:  `platform` and  `port_number`.

These parameters allow the UI to be used across all platforms with the USB explorer for the XBee radios.


**Sample Runs**:  
`python application.py u 7`  
This would result in the serial port trying to open at `\dev\ttyUSB7`

`python application.py w 5`  
This would result in the serial port trying to open at
`COM5`

### Parameters

`platform` refers to the operating system you are running on.


`port_number` refers to the number of the COM port or ttyUSB you are connecting to on the host computer.

|key|platform|
---|---
u|unix (mac, linux,etc.)
w|windows
uw|bash on windows (build 16299 and later)



If you get permission issues on unix, try running it as superuser.

## Arduino Server
Arduino code for wireless hybrid engine ignition test rig.

The igniter software is a state machine that is controlled by input from the serial port.  
In our case, the serial port is used by an XBEE pro 900HP radio, giving us wireless control of the igniter.

### State Machine

The state machine has 6 states it can be in, each corresponding to a number:

State|Number|Green LED|Red LED|Action
:---:|:---:|:---:|:---:|---
`STOP`|1|ON|OFF|Close the valve, turn the igniter relay off.
`IGNITE`|2|OFF|ON|Turn the igniter relay on, starting the igniter.
`OPEN`|3|ON|ON|Keep the igniter relay on, open the valve, keep it open for 10 seconds
`CLOSE`|4|ON|OFF|Close the valve
`WAIT`|5|ON|OFF|Do nothing
`PING`|6|---|---|Send ``"I AM ALIVE!"`` to the base station over the radio

The state machine is written such that the user can go to  the `STOP` state from any of the other states at any time. This is a safety feature, so that the engine test can be aborted and stopped at any time.

### State Transitions
The igniter starts in the `CLOSE` state.  It waits to receive serial input.

The following are two typical state flows:
###### Complete Run
1. Power on -> `CLOSE`
2. User presses `ping` button at base station -> `PING`
3. User presses `start` button at base station -> `IGNITE`
4. Automatic transition: `IGNITE`->`OPEN`
5. Valve opens and stays open for 10 seconds
6. Automatic transition: `OPEN`->`CLOSE`
7. Automatic transition: `CLOSE`->`WAIT`

###### Aborted Run
1. Power on -> `CLOSE`
2. User presses `ping` button at base station -> `PING`
3. User presses `start` button at base station -> `IGNITE`
4. Automatic transition: `IGNITE`->`OPEN`
5. **User presses `stop` button at any time during any state -> `STOP`**
6. Automatic transition: `STOP`->`CLOSE`
7. Automatic transition: `CLOSE`->`WAIT`


### Radio information:
An Xbee Pro 900HP radio is used both for the igniter and the base station.

The XBee packet includes a checksum, which ensures that the data received by one XBee is the same as the data sent by the other XBee.

Parameter|Value|
---|---  
Specified Outdoor Range|	10 Kbps: up to 9 miles (14 km) ( w/ 2.1 dB dipole antennas)
Tested Range | 100m
Range to be used | 50m
Transmit Power|	Up to 24 dBm (250 mW)  
Receiver Sensitivity	| -110 dBm @ 10 Kbps
