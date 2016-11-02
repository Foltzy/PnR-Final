import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''


class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    MIDPOINT = 91
    STOP_DIST = 20
    speed = 100
    TURNSPEED = 195

    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        print("----------- MENU -------------")
        menu = {"1": (" Navigate forward", self.nav),
                "2": (" Rotate", self.rotate),
                "3": (" Dance", self.dance),
                "4": (" Calibrate", self.calibrate),
                "5": (" Test Drive", self.testDrive),
                "6": (" Test Scan", self.chooseBetter),
                "s": (" Status", self.status),
                "q": (" Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

##############################################
############# A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        ##varibles for spin code/dance code
        x = 100
        a = 0
        ##loop: check if clear
        while a <= 100:
            if not self.isClear():
                stop()
                break
            ###if clear then move in "circle" and "dance"
            else:
                self.encR(6)
                a += 25
                while x <= 200 and a == 100:
                    #### Print speed
                    print("------------------------------")
                    print('Speed is set too: ' + str(x))
                    print("------------------------------")
                    servo(40)
                    set_speed(x)
                    self.encB(5)
                    self.encR(18)
                    self.encL(7)
                    servo(30)
                    self.encF(5)
                    servo(60)
                    servo(100)
                    servo(60)
                    servo(100)
                    servo(60)
                    time.sleep(.5)
                    self.encR(7)
                    self.encF(2)
                    servo(120)
                    self.encL(5)
                    self.encR(18)
                    self.encL(18)
                    servo(50)
                    time.sleep(.1)
                    x += 25

################################################
###### Battery STATUS
    def status(self):
        print("------------------------------")
        print("My power is at " + str(volt()) + " volts")
        print("------------------------------")
        self.encF(9)

#################################################
######## TODO List
    #TODO - Test codeing and make bug fixes
    #TODO - Change the stop distance to fix hitting a box
    #TODO - "Division" for motor calibration

#################################################
############ TEST DRIVE Method
    def testDrive(self):
        print("Moving straight!")
        fwd()
        while True:
            if us_dist(15) < self.STOP_DIST:
                ##tell me when he wants to stop
                print("STOP!")
                break
            time.sleep(.05)
            print("Seems alright...")
        self.stop()

    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #loop: check that it's clear
        set_left_speed(100)
        set_right_speed(115)
        while True:
            while self.isClear():
                ##move forward a fine amount while check loop
                self.testDrive()
                ##isClear MVP method
            answer = self.choosePath()
            if answer == "left":
                self.encL(5)
            elif answer == "right":
                self.encR(5)

##############################################
########### Choose path
    def chooseBetter(self):
        self.flushScan()
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60, 2):
            servo(x)
            time.sleep(.1)
            self.scan[x] = us_dist(15)
            time.sleep(.05)
        count = 0
        option = [0]
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60, 2):
            if self.scan[x] > self.STOP_DIST:
                count += 1
            else:
                count = 0
            if count > 9:
                print("Found an option from " + str(x - 20) + " to " + str(x) + " degrees")
                count = 0
                option.append(x)
        count = 0
        for x in option:
            print(" Choice " + str(count) + " is at " + str(x) + " degrees. ")
            count += 1

        ans = input("Your selection: ")
        option.get(ans, [None, error])[1]()

        # TODO figure out what option is closest to the midpoint

##########################################################
####### Calibration methods and turn speed help
    def setSpeed(self, x):
        self.speed = x
        set_left_speed(self.speed * .3)
        set_right_speed(speed)

    def getSpeed(self):
        return self.speed

########################################################
########## Consistent turns
    def turnR(self, x):
        previous = self.getSpeed()
        self.setSpeed(self.TURNSPEED)
        self.encR(x)
        self.setSpeed(previous)

    def turnL(self, x):
        previous = self.getSpeed()
        self.setSpeed(self.TURNSPEED)
        self.encL(x)
        self.setSpeed(previous)

####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
