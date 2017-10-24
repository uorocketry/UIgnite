

def configure_usb(platform, port_number):

    # the usb port will be configured as either COMXXX or TTYUSBXXX
    ser = 0
    if (platform == 'u'):
        ser = "/dev/ttyUSB%s" % port_number # open serial port

    elif(platform == 'w'):
        ser = "COM%s"% port_number

    elif(platform == 'uw'):
        ser = "/dev/ttyS%s"% port_number
    return ser
