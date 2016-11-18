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
    STOP_DIST = 25
    speed = 100
    TURNSPEED = 195

    turn_track = 0.0
    TURN_PER_DEGREE = 0.011
    TURN_MODIFIER = .5

    # CONSTRUCTOR
    def __init__(self):
        print("\033[1;34;40mPiggy has be instantiated!")
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
        print("\033[0;37;40m----------= MENU =------------ \033[1;31;40m")
        menu = {"1": (" Navigate forward", self.nav),
                "2": (" Rotate", self.rotate),
                "3": (" Dance", self.dance),
                "4": (" Calibrate", self.calibrate),
                "5": (" Test Drive", self.testDrive),
                "6": (" Test Scan", self.chooseBetter),
                "c": (" Color Key", self.colorCode),
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
                    print("\033[1;34;40m------------------------------")
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
        print("\033[1;34;40m------------------------------")
        print("My power is at " + str(volt()) + " volts")
        print("------------------------------")

#################################################
######## TODO List
    #TODO - Test coding and make bug fixes

#################################################
############ TEST DRIVE Method
    def testDrive(self):
        print("\033[1;34;40m------------------")
        print("Heading straight!")
        print("------------------")
        fwd()
        while True:
            if us_dist(15) < self.STOP_DIST:
                ##tell me when he wants to stop
                print("STOP!")
                break
            time.sleep(.05)
            print("\033[1;34;40m------------------")
            print("Seems alright...")
            print("------------------")
        self.stop()

############################################################
################# NEW TURN METHOD
    ### encR and encL don't work
    def turnR(self, deg):
        ## Amount of turn
        print("\033[1;34;40m")
        self.turn_track += deg
        ## print exit location
        print("The exit is " + str(self.turn_track) + " degrees away.")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER,
                      self.RIGHT_SPEED * self.TURN_MODIFIER)
        right_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        # return speeds set earlier
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)


    def turnL(self, deg):
        ## Amount of turn
        print("\033[1;34;40m")
        self.turn_track -= deg
        print("The exit is " + str(self.turn_track) + " degrees away.")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER,
                      self.RIGHT_SPEED * self.TURN_MODIFIER)
        left_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        # return speeds set earlier
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def setSpeed(self, left, right):
        set_left_speed(int(left))
        set_right_speed(int(right))
        time.sleep(.05)



#######################################################
################ NAV
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #loop: check that it's clear
        set_left_speed(100)
        set_right_speed(115)
        while True:
            while self.isClear():
                ## move forward a fine amount while check loop
                self.testDrive()
                ## isClear MVP method
            answer = self.choosePath()
            ## Turn right from a specific degree
            if answer == "left":
                self.turnL(45)
            elif answer == "right":
                self.turnR(45)

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
                print("\033[1;34;40m-------------------------------------")
                print("Found an option from " + str(x - 20) + " to " + str(x) + " degrees")
                print("-------------------------------------")
                count = 0
                option.append(x)
                self.dataBase()

        ###print(" Choice " + str(count) + " is at " + str(x) + " degrees. ")

    def dataBase(self):
        print("\033[1;32;40m")
        print("\033[0;37;40m----------- MENU ------------- \033[1;32;40m ")
        menu = {"1": (" Direction Left Four", self.leftTurn4),
                "2": (" Direction Left Two", self.leftTurn2),
                "3": (" Direction Forward Four", self.forward4),
                "4": (" Direction Forward Eight", self.forward8),
                "5": (" Direction Right Two", self.rightTurn2),
                "6": (" Direction Right Four", self.rightTurn4),
                "q": (" Return to selection menu", self.handler)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):

            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

        #ans = input("Your selection: ")
        #option.get(ans, [None, error])[1]()

    def rightTurn4(self):
        self.encR(4)

    def rightTurn2(self):
        self.encR(2)

    def leftTurn4(self):
        self.encL(4)

    def leftTurn2(self):
        self.encL(2)

    def forward4(self):
        self.encF(4)

    def forward8(self):
        self.encF(8)
        # TODO figure out what option is closest to the midpoint

########################################################
########### Color Key
    def colorCode(self):
        print("\033[0;37;40m---------------- Key --------------------")
        print("\033[1;31;40mBright Red = Normal Menu")
        print("\033[1;32;40mBright Green = Selection Menu")
        print("\033[1;34;40mBright Blue = Execution Code")

##########################################################
####### Calibration methods and turn speed help
    def getSpeed(self):
        return self.speed

########################################################
########## Consistent turns
'''
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
'''

####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
