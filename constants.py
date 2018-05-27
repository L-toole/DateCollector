import wallaby as w

# Time
startTime = -1

# Motor ports
LMOTOR = 3
RMOTOR = 0

# Digital ports
CLONE_SWITCH = 9
RIGHT_BUTTON = 13

#isClone = w.digital(CLONE_SWITCH)
isClone = True

# Servos
servoArmBin = 0
servoArmPoms = 1
servoClawPoms = 2

#camera channels
ORANGE = 0
RED = 1
GREEN = 2
YELLOW = 3

#color tolerances
COLOR_PROXIMITY=20
ORANGE_AREA=500
RGY_AREA=100

#Tophat
FRONT_TOPHAT = 0
onBlack = 3000

# Servo Positions
armUp = 100
armDown = 970
pomArmOut = 2000
pomArmBack = 900
pomClawClosed = 1100
pomClawOpen = 0