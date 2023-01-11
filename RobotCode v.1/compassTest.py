import board
import adafruit_lsm303_accel
import adafruit_lsm303dlh_mag
import math
import time

i2c = board.I2C()
mag = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
accel = adafruit_lsm303_accel.LSM303_Accel(i2c)
def magCalibration(mag):
    mag_x, mag_y, mag_z = mag
    correctedX = (mag_x -17.22727272727273)*1.1075638176062503
    correctedY = (mag_y - -6.4090909090909065)*0.8374840845429082
    correctedZ = (mag_z - -21.836734693877553)*1.1073400673400673
    return correctedX, correctedY, correctedZ

def accelCalibration(accel):
    accel_x, accel_y, accel_z = accel
    correctedX = (accel_x -0.19122967499999977)*0.9477011494252874
    correctedY = (accel_y -1.8931737825)*0.8996181123840697
    correctedZ = (accel_z -1.4150995949999992)*1.2001455604075693
    return correctedX, correctedY, correctedZ
    

#for i in range(0,500):
 #   print("Acceleration (m/s^2): X = %0.3f Y = %0.3f Z = %0.3f" %accel.acceleration)
def compassHeading():
    for i in range(0,5000):
    
        #print("Magnetometer (micro-Teslas):
        #X = %0.3f Y = %0.3f Z = %0.3f" %mag.magnetic)
        M = mag.magnetic
        #print(M)
        M = magCalibration(M)
        #angle = math.atan2(M[1],M[0])*180/math.pi
        #print(angle)
        A = accel.acceleration
        A = accelCalibration(A)
        AMag = math.sqrt((A[0]**2) + (A[1]**2)+(A[2]**2))
        ANormX = A[0]/AMag
        ANormY = A[1]/AMag
        ANormZ = A[2]/AMag
        p = math.asin(-ANormX) #Pitch
        r = math.asin(ANormY/math.cos(p))#Roll
        MMag = math.sqrt((M[0]**2) + (M[1]**2)+(M[2]**2))
        MNormX = M[0]/MMag
        MNormY = M[1]/MMag
        MNormZ = M[2]/MMag
        x = MNormX*math.cos(p)+MNormZ*math.sin(p)
        y = MNormX*math.sin(r)*math.cos(p)+MNormY*math.cos(r)-MNormZ*math.sin(r)*math.cos(p)
        z = -MNormX*math.cos(r)*math.sin(p)+MNormY*math.sin(r)+MNormZ*math.cos(r)*math.sin(p)
        Magnitude = math.sqrt(x**2 + y**2+ z**2)
        heading = math.atan2(y,x)*180/math.pi
        #print('Heading: ',  heading,  'Mag: ', Magnitude)
        return heading

#for x in range(1,100):
 #   h = compassHeading()
  #  print(h)
   # time.sleep(0.5)
##magnetometer offsets:  (17.22727272727273, -6.4090909090909065, -21.836734693877553)
##magentometer scaling:  1.1075638176062503 0.8374840845429082 1.1073400673400673
##accel offsets:  (0.19122967499999977, 1.8931737825, 1.4150995949999992)
##accel scaling:  0.9477011494252874 0.8996181123840697 1.2001455604075693
