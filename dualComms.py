import serial

#change following port names as needed
s1 = serial.Serial('/dev/ttyUSB0', 115200)
s2 = serial.Serial('/dev/ttyACM0', 115200)

def loop():
    while True:
        inp = s1.readline()
        inp = str(inp, 'utf-8')
        inp = inp.split(',')
        state  = inp[3]
        s2.write(state)


if __name__ == "__main__":
    loop()