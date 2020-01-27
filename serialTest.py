import serial
import time
 
s = serial.Serial('/dev/ttyUSB0', 9600) # change name, if needed
try:
    s.open()
except:
    pass
time.sleep(5) # the Arduino is reset after enabling the serial connection, therefore we have to wait some seconds
response = ""
try:
    print("Running")
    while True:
        response = s.readline()
        # if response != new_response:
        #     print(response)
        print(response)
except KeyboardInterrupt:
    s.close()

    

# s.write("test")
# try:
#     while True:
#         response = s.readline()
#         print(response)
# except KeyboardInterrupt:
#     s.close()