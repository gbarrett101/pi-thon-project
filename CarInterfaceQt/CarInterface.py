from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time

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

buttonPushed = False #variable to keep track of the button state
frontDoorDistance = 1
rearDoorDistance = 2
threshold = 10


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    
    index = 0
    
    try:#try statement to look out for keeyboard interupts 
        while len(s.readline())>0:
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()

            response = s.readline()
            response = response.split(',')
            distance, speed = response
            if not isSafe(distance, speed, threshold, frontDoorDistance) and index != 3:
                index = 3
                ui.setupUi(Dialog, index)
                Dialog.show()

            index = int(input('Mode: '))
    except KeyboardInterrupt:
        s.close()

    sys.exit(app.exec_())