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
    TURNSPEED = 195
    ## Turn method variables
    turn_track = 0.0
    scan = [None] * 180
    ## Turn method var.
    TIME_PER_DEGREE = 0.011
    TURN_MODIFIER = .45

    # CONSTRUCTOR
    def __init__(self):
        ## Color codes added for understanding "\033[1;34;40m"
        print("\033[1;34;40mPiggy has be instantiated!")
        ## this method makes sure Piggy is looking forward
        ## self.calibrate()
        ## let's use an event-driven model, make a handler of sorts to listen for "events"
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
                "5": (" Test Drive", self.cruise),
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
    #TODO - Test turn track and log all turns

#################################################
############ TEST DRIVE Method
    def cruise(self):
        # Extra credit: Upgrade this so it looks around while driving
        # Use the GoPiGo API's method to aim the sensor forward
        servo(self.MIDPOINT)
        #give the robot time to move
        time.sleep(.05)
        # start driving forward
        fwd()
        # start an infinite loop
        while True:
            # break the loop if the sensor reading is closer than our stop dist
            if us_dist(15) < self.STOP_DIST:
                break
            #YOU DECIDE: How many seconds do you wait in between a check?
            time.sleep(.05)
        # stop if the sensor loop broke
        self.stop()

############################################################
################# TURN METHOD
    ### encR and encL don't work - not efficient options
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
### This runs the entire loop. This is the central logic loop.
######################## NAV
    def nav(self):
        print("\033[1;34;40m")
        print("----------= NAVIGATING! =----------")
        print("Piggy nav")
        print("----------= NAVIGATING! =----------")
        ##### WRITE YOUR FINAL PROJECT HERE
        ## loop: check that it's clear
        ## Running app loop
        while True:
            while self.isClear():
                ## move forward a fine amount while check loop
                self.cruise()
                self.backUp()
                ## isClear MVP method
            turn_target = self.kenny()
            if turn_target > 0:
                self.turnR(turn_target)
            else:
                self.turnL(abs(turn_target))

    def kenny(self):
        # Activate our scanner!
        self.wideScan()
        # count will keep track of contigeous positive readings
        count = 0
        # list of all the open paths we detect
        option = [0]
        # YOU DECIDE: What do we add to STOP_DIST when looking for a path fwd?
        SAFETY_BUFFER = 30
        # YOU DECIDE: what increment do you have your wideScan set to?
        INC = 2

        ###########################
        ######### BUILD THE OPTIONS
        # loop from the 60 deg right of our middle to 60 deg left of our middle
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60):
            # ignore all blank spots in the list
            if self.scan[x]:
                # add 30 if you want, this is an extra safety buffer
                if self.scan[x] > (self.STOP_DIST + SAFETY_BUFFER):
                    count += 1
                # if this reading isn't safe...
                else:
                    # aww nuts, I have to reset the count, this path won't work
                    count = 0
                # YOU DECIDE: Is 16 degrees the right size to consider as a safe window?
                if count > (16 / INC) - 1:
                    # SUCCESS! I've found enough positive readings in a row
                    print("---FOUND OPTION: from " + str(x - 16) + " to " + str(x))
                    # set the counter up again for next time
                    count = 0
                    # add this option to the list
                    option.append(x - 8)

        ####################################
        ############## PICK FROM THE OPTIONS - experimental

        # The biggest angle away from our midpoint we could possibly see is 90
        bestoption = 90
        # the turn it would take to get us aimed back toward the exit - experimental
        ideal = -self.turn_track
        print("\nTHINKING. Ideal turn: " + str(ideal) + " degrees\n")
        # x will iterate through all the angles of our path options
        for x in option:
            # skip our filler option
            if x != 0:
                # the change to the midpoint needed to aim at this path
                turn = self.MIDPOINT - x
                # state our logic so debugging is easier
                print("\nPATH @  " + str(x) + " degrees means a turn of " + str(turn))
                # if this option is closer to our ideal than our current best option...
                if abs(ideal - bestoption) > abs(ideal - turn):
                    # store this turn as the best option
                    bestoption = turn
        if bestoption > 0:
            input("\nABOUT TO TURN RIGHT BY: " + str(bestoption) + " degrees")
        else:
            input("\nABOUT TO TURN LEFT BY: " + str(abs(bestoption)) + " degrees")
        return bestoption

    ############################
    ######## BACKUP
    def backUp(self):
        if us_dist(30) < 10:
            print("Too close. Backing up for half a second")
            bwd()
            time.sleep(.5)
            self.stop()

##############################################
############## WIDE SCAN
    def wideScan(self):
        # dump all values
        self.flushScan()
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60, +2):
            servo(x)
            time.sleep(.1)
            scan1 = us_dist(15)
            time.sleep(.1)
            # double check the distance
            scan2 = us_dist(15)
            # if I found a different distance the second time....
            if abs(scan1 - scan2) > 2:
                scan3 = us_dist(15)
                time.sleep(.1)
                # take another scan and average the three together
                scan1 = (scan1 + scan2 + scan3) / 3
            self.scan[x] = scan1
            print("Degree: " + str(x) + ", distance: " + str(scan1))
            time.sleep(.01)

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
            ### Represent options and display them
            if count > 9:
                print("\033[1;34;40m-------------------------------------")
                print("Found an option from " + str(x - 20) + " to " + str(x) + " degrees")
                print("-------------------------------------")
                count = 0
                option.append(x)
                ### Calling dataBase from below
                self.dataBase()

###########################################################
### Helps enforce moving and turning
############ dataBase menu "controller"
    def dataBase(self):
        print("\033[1;32;40m")
        print("\033[0;37;40m----------= MENU =------------ \033[1;32;40m ")
        menu = {"1": (" Direction Left Four", self.leftTurn4),
                "2": (" Direction Left Two", self.leftTurn2),
                "3": (" Direction Forward Four", self.forward4),
                "4": (" Direction Forward Eight", self.forward8),
                "5": (" Direction Right Two", self.rightTurn2),
                "6": (" Direction Right Four", self.rightTurn4),
                "q": (" Return to selection menu", self.handler)
                }
        ## loop and print the menu...
        for key in sorted(menu.keys()):

            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

###################################################
############# Options for dataBase controller (Above)
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
        ## TODO figure out what option is closest to the midpoint

########################################################
########### Color Key
    def colorCode(self):
        print("\033[0;37;40m---------------= Key =-------------------")
        print("\033[1;31;40mBright Red = Normal Menu")
        print("\033[1;32;40mBright Green = Selection Menu")
        print("\033[1;34;40mBright Blue = Execution Code")

########################################################
    ### Intervention between nav and encL/R
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
