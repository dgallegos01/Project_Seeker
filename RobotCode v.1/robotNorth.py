from compassTest import *
from movements import *
def goDirection(direction):
    compass = compassHeading() #Get Compass Bearing
    #direction = 0 # between -180-180
    #heading = 60

    diff = direction - compass #Calculate Difference
    if abs(diff)<10: #Difference less than 10 go straight
        print("Go Straight!")
        moveForward()
        goDirection(direction)
    else:
        if diff >0: #Difference is positive go right else go left
            print("Go Right!")
            turnRight(direction)
            goDirection(direction)
        else:
            print("Go Left!")
            turnLeft(direction)
            goDirection(direction)
