#!/usr/bin/python
import argparse
from Tkinter import *
from Utility import *
import serial
import sys
import time

parser = argparse.ArgumentParser(description='establish serial communication with Serial port based on platform and port no.')
parser.add_argument('platform', help="w -> windows | u-> unix | uw -> bash on windows (build 16299 and later)")
parser.add_argument('port_number', help="if using unix, it is X in ttyUSBX | if using windows, it is X in COMX")
args = parser.parse_args()



def add_text(words, box):
    box.insert(CURRENT, words)
    box.pack()

def ping(serial,message, box):
    add_text("\nPinging Igniter", box)
    serial.write(message)
    add_text("\nwaiting for reply", box)
    try:
        serial.readline()
        add_text("\n IGNITER: %s" % serial.readline(), box)
    except Exception as e:
        add_text( "\nIGNITER: could not read line", box)
    return

def fire(serial, message, box):
    add_text("\nStarting Ignition!",box)
    serial.write(message)
    add_text("\nwaiting for confirmation",box)
    try:
        add_text("\n IGNITER: %s" % serial.readline(), box)
    except Exception as e:
        add_text( "\nIGNITER: could not read line", box)
    return

def stop(serial,message1, message2, box):
    add_text("\nSTOPPING!",box)
    serial.write(message1)
    add_text("\nwaiting for confirmation",box)
    try:
        add_text("\n IGNITER: %s" % serial.readline(), box)
    except Exception as e:
        add_text( "\nIGNITER: could not read line", box)
    time.sleep(0.05)
    add_text("\nCLOSING!", box)
    serial.write(message2)
    add_text("\nwaiting for confirmation",box)
    try:
        add_text("\n IGNITER: %s" % serial.readline(), box)
    except Exception as e:
        add_text( "\nIGNITER: could not read line", box)

    return

def main(argv):
    print (argv)
    temp = (configure_usb(argv[0], argv[1]))
    ser = serial.Serial(temp)
    try:
        ser.close()
        ser.open()
    except Exception as e:
        print("port error")

    root = Tk()
    root.title("UIgnite")
    frame = Frame(root)
    frame.pack()
    topframe = Frame(root)
    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )
    topframe.pack(side = TOP)

    text = Text(bottomframe)
    text.insert(INSERT, "Hello.....")
    text.pack()


    redbutton = Button(topframe, text="STOP", fg="red",command=lambda:stop(ser,"1","5",text))
    redbutton.pack( side = LEFT)
    greenbutton = Button(topframe, text="START", fg="green", command=lambda: fire(ser,"2",text))
    greenbutton.pack( side = LEFT )
    bluebutton = Button(topframe, text="PING", fg="blue", command=lambda: ping(ser,"6",text))
    bluebutton.pack( side = RIGHT )


    root.mainloop()


if __name__ == "__main__":
    #print(sys.argv[1],sys.argv[2])
    main(sys.argv[1:])
