import serial
import time
encoding = 'utf-8'
s = serial.Serial('/dev/ttyUSB0', 115200) # change name, if needed
try:
    s.open()
except:
    pass
time.sleep(5) # the Arduino is reset after enabling the serial connection, therefore we have to wait some seconds
response = ""
print("Running")
while True:
    response = s.readline()
    str(response, 'utf-8')
    print(type(response))
    # if response != new_response:
    #     print(response)
    print(response)

# try:
#     print("Running")
#     while True:
#         response = s.readline()
#         print(type(response))
#         # if response != new_response:
#         #     print(response)
#         print(response)
# except KeyboardInterrupt:
#     s.close()

    

# s.write("test")
# try:
#     while True:
#         response = s.readline()
#         print(response)
# except KeyboardInterrupt:
#     s.close()