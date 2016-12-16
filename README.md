Ben Foltz
Mr. A
PnR 12/14/16
                                        VVVVVVV,           VVVVVVV,
                                        VV   .VV           VV   .VV
                                        VVVVVVV'  VV.VVV.  VVVVVVV'
                                        VV        VV   VV  VV  VV.
                                        VV        VV   VV  VV   VV.
                                               -=[Original]=-

PnR_Final:
This is a project chosen by Mr. A to test our programming knowledge and give us, and him, a challenge. In
this project we have created the code in order to send our robot AI through a hand made maze. Different robots
take different paths that adds to the challenge, along side the code. There are many creative aspects you can
change about this robot and it's code. As an example, I changed the color of my code in order to make it easier
to read when in 'putty.' Overall, this project was just about messing around with turn degrees and motor speeds.


Some of our methods:
self.wideScan() - The wideScan method is just that, a wide scan. Starting at degree '60' and going to degree '-60'
this is a thorough scan.

self.scan() - The scan method is a lot like the wideScan. Although, the difference is how large the scan is. This
method can be changed using the variable 'x' iun order to have a custom scan.

self.backUp() - When inside the specified range the robot will back up in order to dodge the obstacle. This is also
a variable that can be changed making it easy to control.

self.STOP_DIST - This is the built in natural stop distance. Without this the robot would never stop, therefore
hitting almost everything in it's path.

self.stop() - This is also a simple method in order to stop the robot and all it's actions. For example, if the
robot is scanning and you run this method, it will stop the scan and if it's moving it'll stop moving.

self.setSpeed() - Set speed is an easy way to change the speed of your robot when it's moving or executing code.
It's used in the calibrate method, that's explained below.

self.calibrate() - Calibrate is a method run our menu that allows you to change all the motor speeds and angles
of the servo.


Some of my custom methods:
\033[0;37;40m 'message' - This is the custom color codes that I have implemented to make my code more readable.

self.leftTurn4(), self.forward4() - These were added to my secondary menu in order to 'control' the robot from
your computer. This will pop up as green in 'putty.'

self.colorCode() - This is a main menu option that allows a new user to see what a specific color means in 'putty.'
Most simply just brings up a colored menu for more information about colors.

self.dataBase() - As mentioned earlier, this is the secondary menu I created using the main menu. It is named
'dataBase' because it needed a separate name in order to run. Brings up a selection menu in order to run certain
'encR' or 'encL' commands.

self.kenny() - This is the main turn method. This controls every turn and paths the robot could take to get to it's
exit. This is custom because it was changed to fit the needs of my robot, as in adding a '2000 degree' turning angle
as a guarantee fot the correct option.


Ideas for the future:
In the future I would like to find a purpose for this robot. For example, we can make this robot find the nearest water
source in order to save people that have no water. There are other things we can do with this robot along these lines.
Although each would take a bit more programming in order to accomplish.


Issues:
There were way too many issues that arose with this project. One issue was with 'encR' and 'encL.' These methods were
not making accurate turns and only turning at a given number verses a certain degree. For example, the robot would
always turn 45 degrees with encR but with the updated 'kenny' method it will locate the exit and base it's turn off
of how many degrees away the exit is. Another problem came when we were editing the menu and adding new methods to it.
When making a new menu I needed to rename it to distinguish the menu from the fist. My secondary menu is named 'dataBase'
and my first is named 'handler.'

