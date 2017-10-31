# UIgnite

 A basic UI made with Tkinter in python 2.7 for controlling engine ignition tests via XBee radios.  
 Built to work with Arduino-Iginiton.
![screen shot 2017-10-25 at 10 24 07 am](https://user-images.githubusercontent.com/20449016/32208520-664bc2a6-bdd9-11e7-882c-718dc20fb6dc.png)
## Running
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

## Parameters

`platform` refers to the operating system you are running on.


`port_number` refers to the number of the COM port or ttyUSB you are connecting to on the host computer.

|key|platform|
---|---
u|unix (mac, linux,etc.)
w|windows
uw|bash on windows (build 16299 and later)



If you get permission issues on unix, try running it as superuser.
