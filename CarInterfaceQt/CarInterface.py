from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
from playsound import playsound


#Open the serial port
s = serial.Serial('/dev/ttyUSB0', 115200) # change name, if needed
try:   
    s.open()
except:
    pass
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
    
    if speed <= 0:
        time = float('inf')
    else:
        time = (distance-doorPosition)/speed
    if time < threshold:
        return False
    return True



class Ui_Dialog(object):
    def setupUi(self, Dialog, index = 0):
        Dialog.setObjectName("CarInterface")
        Dialog.resize(800, 484)
        Dialog.setAutoFillBackground(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(420, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        
        

        self.CarWidgets = QtWidgets.QStackedWidget(Dialog)
        self.CarWidgets.setGeometry(QtCore.QRect(0, 0, 801, 321))
        self.CarWidgets.setObjectName("CarWidgets")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 321))
        self.label.setObjectName("label")

        self.CarWidgets.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 851, 321))
        self.label_2.setObjectName("label_2")
        self.CarWidgets.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 801, 321))
        self.label_3.setObjectName("label_3")
        self.CarWidgets.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 801, 321))
        self.label_4.setObjectName("label_4")
        self.CarWidgets.addWidget(self.page_4)

        self.TextOut = QtWidgets.QLabel(Dialog)
        self.TextOut.setGeometry(QtCore.QRect(0, 321, 40, 360))
        self.TextOut.setText("hello world")
        self.TextOut.setObjectName(("TextOut"))
  

        self.retranslateUi(Dialog)
        self.CarWidgets.setCurrentIndex(index)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CarInterface"))
        
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/Car0.1.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/Car1.1.png\"/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/Car2.1.png\"/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/Car3.1.png\"/></p></body></html>"))
        self.TextOut.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/Car2.1.png\"/></p></body></html>"))

import QtDesign_rc

buttonState = 0
newButtonState = 0
buttonPushed = False #variable to keep track of the button state
frontDoorDistance = 1
rearDoorDistance = 2
threshold = 10


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    index = 0
    
    try:#try statement to look out for keyboard interupts 
        while len(s.readline())>0:
            print("loop going")
            response = s.readline()
            response = str(response, 'utf-8')
            response = response.split(',')
            speed = response[0]
            distance = response[1]
            signalStrength = response[2]
            #code for the button that will initially be commented out
            #newButtonState = response[3]
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
                ui.setupUi(Dialog, index)
                Dialog.show()
            elif index != 0 and isSafe(distance, speed, threshold, frontDoorDistance):
                #scenario where the car is safe but it wasn't before
                playsound('leftClear.mp3')
                buttonPushed = False
                index = 0
                ui.setupUi(Dialog, index)
                Dialog.show()
            buttonState = newButtonState
        s.close()

    except KeyboardInterrupt:
        pass

    sys.exit(app.exec_())