from compassTest import *
from movements import *
def goDirection(direction):
    compass = compassHeading() #Get Compass Bearing
    #direction = 0 # between -180-180

    diff = direction - compass #Calculate Difference

    if abs(diff)<10: #Difference less than 10 go straight
        print("Go Straight!")
        moveForward()
        goDirection(0)
    else:
        if diff >0: #Difference is positive go right else go left
            print("Go Right!")
            turnRight(direction)
            goDirection(0)
        else:
            print("Go Left!")
            turnLeft(direction)
            goDirection(0)
