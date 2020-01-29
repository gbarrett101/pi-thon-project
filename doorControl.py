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

def loop():
    index = 0
    while len(s.readline())>0:
            print("loop going")
            response = s.readline()
            response = str(response, 'utf-8')
            response = response.split(',')
            speed = response[0]
            distance = response[1]
            signalStrength = response[2]
            #code for the button that will initially be commented out
            newButtonState = response[3]
            speed = float(speed) #in cm/sec
            distance = int(distance) #in cm
            signalStrength = int(signalStrength)
            if newButtonState == 0 and buttonState == 1:
                buttonPushed = True
                if isSafe(distance, speed, threshold, frontDoorDistance) :
                    #maybe say something here
                    buttonPushed = False
                else:
                    playsound('wait.mp3')
            if not isSafe(distance, speed, threshold, frontDoorDistance) and index != 3:
                #scenario where the car is not safe but previously before 
                index = 3
            elif index != 0 and isSafe(distance, speed, threshold, frontDoorDistance):
                #scenario where the car is safe but it wasn't before
                if buttonPushed:
                    playsound('leftClear.mp3') #more audio feedback stuff
                buttonPushed = False
                index = 0
            buttonState = newButtonState


buttonState = 0
newButtonState = 0
buttonPushed = False #variable to keep track of the button state
frontDoorDistance = 1
rearDoorDistance = 2
threshold = 10


try: #try statement to look out for keeyboard interupts 
    loop()
except KeyboardInterrupt:
    s.close()

