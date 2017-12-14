"""Using pygame to read in ds4 controller
with ds4drv  running as a daemon
DS4  controller axis maps:
Axis0: Left stick l-r (-1 left, 1 right)
Axis1: Left stick u-d (-1 up, 1 down)
Axis2: Right stick l-r (-1 left, 1 right)
Axis5: Right stick u-d (-1 up, 1 down)
Axis4: Right trigger (-1 unpressed, 1 completely pressed)
"""
import socket, struct, time
import pygame
from modules.utils import *

#initialise DS4 controller
update_rate = 0.01 # 100 hz loop cycle

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

if(joystick.get_name()=='Sony Computer Entertainment Wireless Controller'):
    print("DS4 connected")
else:
    print("Not a DS4")

while True:
    current = time.time()
    elapsed = 0
    pygame.event.pump()
    pygame.event.get()
    #roll = joy.get_axis(2)
    #pitch = joy.get_axis(1)
    #yaw = joy.get_axis(0)
    #thr = joy.get_axis(4)
    arm = joystick.get_button(9)
    roll     = mapping(joystick.get_axis(2),-1.0,1.0,1000,2000) #The ranges of values for baseflight/cleanflight are between 1000-2000 whit 1500 neutral)
    pitch    = mapping(joystick.get_axis(1),1.0,-1.0,1000,2000)
    yaw      = mapping(joystick.get_axis(0),-1.0,1.0,1000,2000)
    throttle = mapping(joystick.get_axis(4),-1.0,1.0,1000,2000)
    print(roll)
    print(pitch)
    print(yaw)
    print(throttle)
    print(arm)
    while elapsed < update_rate:
        elapsed = time.time() - current
