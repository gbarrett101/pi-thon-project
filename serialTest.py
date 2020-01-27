import serial
import time
 
s = serial.Serial('/dev/ttyACM0', 9600) # change name, if needed
# s.open()
time.sleep(5) # the Arduino is reset after enabling the serial connection, therefore we have to wait some seconds
response = ""
while True:
    new_response = s.readline()
    if response != new_response:
        print(response)
    response = new_response

    

# s.write("test")
# try:
#     while True:
#         response = s.readline()
#         print(response)
# except KeyboardInterrupt:
#     s.close()