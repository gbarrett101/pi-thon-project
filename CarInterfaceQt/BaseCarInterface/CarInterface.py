# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarInterface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
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

        self.retranslateUi(Dialog)
        self.CarWidgets.setCurrentIndex(0)
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

import QtDesign_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

