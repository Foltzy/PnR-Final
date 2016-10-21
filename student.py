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
                "4": (" Calibrate servo", self.calibrate),
                "s": (" Status", self.status),
                "q": (" Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    # A SIMPLE DANCE ALGORITHM
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

    def status(self):
        print("------------------------------")
        print("My power is at " + str(volt()) + " volts")
        print("------------------------------")

    #################################################
    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #TODO: If while loop fails, check for other paths
        #loop: check that it's clear
        while self.isClear():
            ##move forward a fine bit while check loop
            self.encF(10)
        else:
            self.choosePath()
            while True:
                ##isClear MVP method
                answer = self.choosePath()
                if answer == "left":
                    self.encL(4)
                elif answer == "right":
                    self.encR(4)



####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
