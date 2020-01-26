import serial
import time

#Open the serial port
s = serial.Serial('/dev/ttyACM0', 9600) # change name, if needed
s.open()
time.sleep(5) # the Arduino is reset after enabling the serial connection, therefore we have to wait some seconds

def isSafe(distance, speed, threshold, doorPosition):
    """
    Parameters:
    distance - distance object is away from sensor
    speed - velocity at which the object is travelling
    threshold - willing tolerance of time for it to be deemed as safe to exit the vehicle
    doorPosition - distance the door is away from the sensor 

    Returns:
    boolean - True if it is safe to exit, false if it is not
    """
    time = (distance-doorPosition)/speed
    if time < threshold:
        return False
    return True

buttonPushed = False #variable to keep track of the button state
frontDoorDistance = 1
rearDoorDistance = 2
threshold = 10


try: #try statement to look out for keeyboard interupts 
    while True:
        response = s.readline()
        response = response.split(',')
        distance, speed = response
        if not isSafe(distance, speed, threshold, frontDoorDistance):
            #make front door red
            pass
        if not isSafe(distance, speed, threshold, rearDoorDistance):
            #make rear door red
            pass
except KeyboardInterrupt:
    s.close()

