import serial
import time
import pygame
import subprocess


#Open the serial port
s = serial.Serial('/dev/ttyUSB1', 115200) # change name, if needed
try:
    s.open()
except:
    pass
time.sleep(5) # the Arduino is reset after enabling the serial connection, therefore we have to wait some seconds

def playAudio(name):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    # subprocess.Popen(['omxplayer','-b', name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)


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
    # Debugging code
    # if distance < 50:
    #     return False
    if speed <= 0:
        time = float('inf')
    else:
        time = (distance-doorPosition)/speed
    if time < threshold:
        return False
    return True

def loop():
    index = 0
    buttonPushed = False
    buttonState = 0
    pygame.mixer.init()
    while len(s.readline())>0:
            response = s.readline()
            response = str(response, 'utf-8')
            response = response.split(',')
            speed = response[0]
            distance = response[1]
            signalStrength = response[2]
            #code for the button that will initially be commented out
            newButtonState = int(response[3])
            # print(newButtonState)
            speed = float(speed) #in cm/sec
            distance = int(distance) #in cm
            signalStrength = int(signalStrength)
            # print(isSafe(distance, speed, threshold, frontDoorDistance))
            if isSafe(distance, speed, threshold, frontDoorDistance):
                s.write(bytes([0]))
            else:
                print(bytes([1]))
                s.write(bytes([1]))
            if newButtonState == 0 and buttonState == 1:
                buttonPushed = True
                print("ran")
                print(isSafe(distance, speed, threshold, frontDoorDistance))
                if isSafe(distance, speed, threshold, frontDoorDistance) :
                    #maybe say something here
                    buttonPushed = False
                else:
                    print("wait")
                    playAudio('wait.mp3')
            if not isSafe(distance, speed, threshold, frontDoorDistance) and index != 3:
                #scenario where the car is not safe but previously before 
                index = 3
            elif index != 0 and isSafe(distance, speed, threshold, frontDoorDistance):
                #scenario where the car is safe but it wasn't before
                if buttonPushed:
                    playAudio('leftClear.mp3') #more audio feedback stuff
                buttonPushed = False
                index = 0
            buttonState = newButtonState


buttonState = 0
newButtonState = 0
buttonPushed = False #variable to keep track of the button state
frontDoorDistance = 1
rearDoorDistance = 2
threshold = 1000


try: #try statement to look out for keeyboard interupts 
    loop()
except KeyboardInterrupt:
    s.close()

