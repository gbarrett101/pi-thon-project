import serial
import time

#change following port names as needed
s2 = serial.Serial('/dev/ttyUSB0', 115200)
s1 = serial.Serial('/dev/ttyACM0', 115200)

try:
    s1.open()
except:
    pass
try:
    s2.open()
except:
    pass
def loop():
    while True:
        inp = s1.readline()
        inp = str(inp, 'utf-8')
        inp = inp.split(',')
        # print(inp)
        state  = inp[0]
        # print(type(state))
        # print(state[0])
        # state = int(state[0])
        # print(state)
        try:
            num = float(state)
            print(num)
            s2.write(num)
        except:
            pass
        # inp2 = s2.readline()
        # inp2 = str(inp, 'utf-8')
        # inp2 = inp.split(',')
        # print(inp2)
        # s2.write(state)


if __name__ == "__main__":
    time.sleep(2)
    loop()